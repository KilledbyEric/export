import json
import logging
import xlsxwriter
from datetime import datetime
from wxcloudrun import settings

from django.http import FileResponse
from django.shortcuts import render
from wxcloudrun.models import exportdata
import os


logger = logging.getLogger('log')


def index(request,_):
    if request.method == 'GET' or request.method == 'get':
    #     return render(request, 'index.html')
    # else:
        timeStamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
        file_name = "志愿表"+timeStamp+".xlsx"
        dest_filename = str(settings.BASE_DIR) + '\\doc_tmp\\' + file_name
        # dest_filename = '.' + '\\doc_tmp\\' + file_name
        wb = xlsxwriter.Workbook(dest_filename)
        ws_list = [wb.add_worksheet('冲'),wb.add_worksheet('稳'),wb.add_worksheet('保')]
        columns = ['院校代码', '院校名称', '专业代码', '专业名称', '专业简注',  '省份', '城市', '本专', '学制', '学费', '2023选考科目', '2022计划数', '2022投档线', '2022投档位次', '第四轮学科评估结果', '办学特色', '办学性质']
                    # 0          1           2           3         4          5        6     7       8       9         10            11             12             13               14               15         16               
        idx = 0
        for ws in ws_list:
            row_num = 0
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num])
            dataList = request.GET.get('list'+str(idx)).split(",")
            
            rows = exportdata.objects.filter(id__in = dataList).values_list()
            # ['wishData0001003', '浙江大学(一流大学建设高校)', '外国语言文学类', '含英语、翻译专业。', 4, '浙江', '杭州', '本科', '5300', '不限', 10, 665, 3044, 'A', '985', '公办']
            #              0                 1                      2                    3          4    5      6        7      8      9      10  11    12    13   14    15                            
            for row in rows:
                row_num += 1
                row = list(row)
                for col_num in range(len(row)):
                    ws.write(row_num, 0, row[0][-7:-3])
                    ws.write(row_num, 1, row[1])
                    ws.write(row_num, 2, row[0][-3:])
                    ws.write(row_num, 3, row[2])
                    ws.write(row_num, 4, row[3])
                    ws.write(row_num, 5, row[5])
                    ws.write(row_num, 6, row[6])
                    ws.write(row_num, 7, row[7])
                    ws.write(row_num, 8, row[4])
                    ws.write(row_num, 9, row[8])
                    ws.write(row_num, 10, row[9])
                    ws.write(row_num, 11, row[10])
                    ws.write(row_num, 12, row[11])
                    ws.write(row_num, 13, row[12])
                    ws.write(row_num, 14, row[13])
                    ws.write(row_num, 15, row[14])
                    ws.write(row_num, 16, row[15])
            idx += 1

        
    wb.close()
    excel = open(dest_filename,"rb")
    # FileResponse 该类可以将文件下载到浏览器
    response = FileResponse(excel)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
    os.remove(dest_filename)
    return response

 

# def counter(request, _):
#     """
#     获取当前计数

#      `` request `` 请求对象
#     """

#     rsp = JsonResponse({'code': 0, 'errorMsg': ''}, json_dumps_params={'ensure_ascii': False})
#     if request.method == 'GET' or request.method == 'get':
#         rsp = get_count()
#     elif request.method == 'POST' or request.method == 'post':
#         rsp = update_count(request)
#     else:
#         rsp = JsonResponse({'code': -1, 'errorMsg': '请求方式错误'},
#                             json_dumps_params={'ensure_ascii': False})
#     logger.info('response result: {}'.format(rsp.content.decode('utf-8')))
#     return rsp


# def get_count():
#     """
#     获取当前计数
#     """

#     try:
#         data = Counters.objects.get(id=1)
#     except Counters.DoesNotExist:
#         return JsonResponse({'code': 0, 'data': 0},
#                     json_dumps_params={'ensure_ascii': False})
#     return JsonResponse({'code': 0, 'data': data.count},
#                         json_dumps_params={'ensure_ascii': False})


# def update_count(request):
#     """
#     更新计数，自增或者清零

#     `` request `` 请求对象
#     """

#     logger.info('update_count req: {}'.format(request.body))

#     body_unicode = request.body.decode('utf-8')
#     body = json.loads(body_unicode)

#     if 'action' not in body:
#         return JsonResponse({'code': -1, 'errorMsg': '缺少action参数'},
#                             json_dumps_params={'ensure_ascii': False})

#     if body['action'] == 'inc':
#         try:
#             data = Counters.objects.get(id=1)
#         except Counters.DoesNotExist:
#             data = Counters()
#         data.id = 1
#         data.count += 1
#         data.save()
#         return JsonResponse({'code': 0, "data": data.count},
#                     json_dumps_params={'ensure_ascii': False})
#     elif body['action'] == 'clear':
#         try:
#             data = Counters.objects.get(id=1)
#             data.delete()
#         except Counters.DoesNotExist:
#             logger.info('record not exist')
#         return JsonResponse({'code': 0, 'data': 0},
#                     json_dumps_params={'ensure_ascii': False})
#     else:
#         return JsonResponse({'code': -1, 'errorMsg': 'action参数错误'},
#                     json_dumps_params={'ensure_ascii': False})
