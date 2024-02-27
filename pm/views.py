import logging

from django.core.serializers import json
from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from myapp.models import Question
from pm.models import ProjectInfo
from pmmonkey.entities.models import *
from django.http.response import HttpResponse, JsonResponse
from django.conf import  settings
logger = logging.getLogger(__name__)
def add(request):
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
    pmInfo = request.body
    pm = ProjectInfo()
    pm.addPM(pmInfo)

    return  JsonResponse(resp, status=200)
