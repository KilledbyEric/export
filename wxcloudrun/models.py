from datetime import datetime

from django.db import models


# # Create your models here.
# class Counters(models.Model):
#     id = models.AutoField
#     count = models.IntegerField(max_length=11, default=0)
#     createdAt = models.DateTimeField(default=datetime.now(), )
#     updatedAt = models.DateTimeField(default=datetime.now(),)

#     def __str__(self):
#         return self.title

#     class Meta:
#         db_table = 'Counters'  # 数据库表名


class exportdata(models.Model):
    id = models.CharField(max_length=20, null=False, blank=False,primary_key=True)
    collageName = models.CharField(max_length=100, null=False, blank=False)
    majorName = models.CharField(max_length=100, null=False, blank=False)
    note = models.CharField(max_length=800, null=True, blank=True)
    schooling = models.SmallIntegerField(max_length=5, null=False, blank=False)
    province = models.CharField(max_length=10, null=False, blank=False)
    city = models.CharField(max_length=10, null=False, blank=False)
    bz = models.CharField(max_length=4, null=False, blank=False)
    tuition = models.CharField(max_length=10, null=False, blank=False)
    xk = models.CharField(max_length=20, null=False, blank=False)
    planNum = models.SmallIntegerField(max_length=4, null=False, blank=False)
    score = models.SmallIntegerField(max_length=3, null=False, blank=False)
    position = models.IntegerField(max_length=7, null=False, blank=False)
    CDR = models.CharField(max_length=2, null=True, blank=True)
    level = models.CharField(max_length=10, null=True, blank=True)
    owner = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = 'exportdata'  # 数据库表名
