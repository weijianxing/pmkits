#-*- coding: utf-8 -*-
# 
# __author__ : jianxing.wei

# Create your models here.
from django.db import models

#用户信息
class User(models.Model):
    role = models.CharField(max_length=128, db_column='前端开发，后端开发，测试，产品经理，项目经理')
    type = models.IntegerField(db_column='1，数科驻场，2，数科本部，3易大宗')
    userid = models.IntegerField(db_index=True, unique=True)

#项目信息
class ProjectInfo(models.Model):
    businessLine = models.CharField(max_length=64, db_column='项目所属业务线')
    description = models.CharField(max_length=255, db_column='项目描述')
    ower = models.IntegerField(db_column='归属')
    progress = models.IntegerField(db_column='进度')
    status = models.IntegerField(db_column='项目状态： 1 进行中， 正常结束， 延期')
    type = models.IntegerField(db_column='1，数科驻场，2，数科本部，3易大宗')
    projectId = models.IntegerField(db_index=True, unique=True)
    startup = models.DateTimeField(db_column= '项目启动时间')
    deadline = models.DateTimeField(db_column='结束时间')

#执行变更
class rojectLog(models.Model):
    logInfo = models.CharField(max_length=255, db_column='跟进信息')
    projectId = models.IntegerField(db_column='关联项目Id')
    logId = models.IntegerField(db_index=True, unique=True)
    logDate = models.DateTimeField(db_column= '记录时间')