import datetime

from django.db import models

# Create your models here.
#-*- coding: utf-8 -*-
#
# __author__ : jianxing.wei

# Create your models here.
from django.db import models

#用户信息
from django.db.models import F

from datetime import datetime
class User(models.Model):
    role = models.CharField(max_length=128, help_text='前端开发，后端开发，测试，产品经理，项目经理')
    type = models.IntegerField(help_text='1，数科驻场，2，数科本部，3易大宗')
    name = models.CharField(max_length=64,default='')
    userID = models.IntegerField(default=0)

#项目信息
class ProjectInfo(models.Model):
    id = models.AutoField(primary_key=True)
    businessLine = models.CharField(max_length=64, help_text='项目所属业务线')
    description = models.CharField(max_length=255, help_text='项目描述')
    ower = models.IntegerField(help_text='归属')
    progress = models.IntegerField(help_text='进度')
    status = models.IntegerField(help_text='项目状态： 1 进行中， 2正常结束， 3延期，4待启动')
    type = models.IntegerField(help_text='1，project，2，task')
    projectId = models.CharField(max_length=64, help_text='项目编号',default='')
    startup = models.DateTimeField(help_text= '项目启动时间')
    deadline = models.DateTimeField(help_text='结束时间')
    parentId = models.IntegerField(help_text='所属父节点', default=0)
    PRDLink = models.CharField(max_length=255, help_text='项目prd link', default='')
    createTime = models.DateTimeField(help_text= '项目创建时间', default=datetime.now())



    def addPM(self, pmInfo):
        """
        添加一条项目信息
        :param pmInfo:
        :return:
        """
        self.businessLine = pmInfo["businessLine"]
        self.description = pmInfo["description"]
        self.ower = pmInfo["ower"]
        self.progress = pmInfo["progress"]
        self.status = pmInfo["status"]
        self.type = pmInfo["type"]
        # self.projectId = pmInfo.projectId
        self.parentId = pmInfo["parentId"]
        self.PRDLink = pmInfo["PRDLink"]
        self.type = pmInfo["type"]
        self.startup = datetime.strptime(pmInfo["startup"], "%Y-%m-%d %H:%M:%S")
        self.deadline = datetime.strptime(pmInfo["deadline"], "%Y-%m-%d %H:%M:%S")
        self.createTime = datetime.now()

        self.save()
    def updatePM(self,pmInfo):
        """
        更新项目执行信息
        :param pmInfo:
        :return:
        """
        # ProjectInfo.objects.update_or_create(pk=pmInfo.projectId,defaults={'status':pmInfo.status})
        ProjectInfo.objects.filter(projectId=pmInfo.projectId).update(status=F(pmInfo.status))


#执行变更
class ProjectLog(models.Model):
    logInfo = models.CharField(max_length=255, help_text='跟进信息')
    projectId = models.IntegerField(help_text='关联项目Id')
    logId = models.IntegerField(db_index=True, unique=True)
    logDate = models.DateTimeField(help_text= '记录时间')