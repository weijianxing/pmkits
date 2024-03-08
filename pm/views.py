import json
import logging

from django.core import serializers
from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.db.models import OrderBy

# Create your views here.
from django.utils import timezone

from myapp.models import Question
from pm.models import ProjectInfo
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

def get_projects(request):
    # request_data = request.body.decode('utf-8')
    infos = ProjectInfo.objects.order_by('-createTime')[:20]
    # logger.info("项目个数： ")
    # for data in infos:
    #     logger.info(serializers.serialize('json', [data]))

    infos_json = serializers.serialize('json', infos)
    logger.info(infos_json)
    return JsonResponse(infos_json, status=200,safe=False)



