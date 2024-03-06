import logging

from django.core.serializers import json
from django.db.models import F
from django.shortcuts import render, get_object_or_404

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

    logger.info(request.body)
    resp = {"status":000,"message":'项目创建成功'}
    if request.method == 'POST':
        try:
            request_data = request.body.decode('utf-8')
            logger.info('添加项目信息')
            logger.debug(request_data)
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
