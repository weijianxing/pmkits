import datetime
import json
import logging

from django.core import serializers
from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.db.models import OrderBy

# Create your views here.
from django.utils import timezone

from myapp.models import Question
from pm.models import ProjectInfo, User
from pmmonkey.entities.models import *
from django.http.response import HttpResponse, JsonResponse
from django.conf import  settings
#取 来自setting中配置

logger = logging.getLogger('django')
# logger.setLevel(logging.INFO)
def add(request):
    # logger.setLevel(logging.INFO)
    # print('===== test add ')
    # print(request.body)
    logger.info("**************************-----add a new project.")


    resp = {"status":000,"message":'项目创建成功'}
    if request.method == 'POST':
        try:
            request_data = request.body.decode('utf-8')
            # logger.info("request.body:" + request_data)
            logger.info('添加项目信息')
            logger.info(request_data)
            pm = ProjectInfo()


            pmdict = json.loads(request_data)
            pm.addPM(pmdict)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    logger.info('添加项目信息')

    return  JsonResponse(resp, status=200)

def update_satus(request):
    ProjectInfo.objects.filter(projectId=request.projectId).update(status=F(request.status))

    # q = get_object_or_404(ProjectInfo, pk=request.id)
    # q.status = request.status
    # q.save()

def getDuration( start: datetime, end: datetime):
    # Get timestamps in seconds
    timestamp_1 = start.timestamp()
    timestamp_2 = end.timestamp()

    # Calculate the difference in seconds
    time_difference = timestamp_2 - timestamp_1

    # Convert to milliseconds
    millisecond_difference = int(time_difference * 1000)
    return millisecond_difference

def get_projects(request):
    #使用order by 过滤条件
    info_projects  = ProjectInfo.objects.order_by('-createTime')[:20]
    # logger.info("项目个数： ")
    # for data in infos:
    #     logger.info(serializers.serialize('json', [data]))
    tasks = []
    for info in info_projects:
        task = {}
        task["id"] = info.id
        print("task id : ", info.id)
        task["label"] = info.description
        user = User.objects.filter(pk=info.ower).first()
        task["parentId"] = info.parentId
        task["user"] = user.name

        task["start"] = info.startup
        task["duration"] = getDuration(info.startup, info.deadline)
        task["percent"] = info.progress
        task["type"] = info.type
        tasks.append(task)

    #print(task)
    # infos_json = serializers.serialize('json', tasks,safe=False)
    infos_json = json.dumps(tasks,default=str, ensure_ascii=False)
    logger.info(infos_json)
    return JsonResponse(infos_json, status=200,safe=False)



