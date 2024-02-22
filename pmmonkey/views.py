#-*- coding: utf-8 -*-
# 
# __author__ : jianxing.wei
from django.utils import timezone

from myapp.models import Question
from pmmonkey.entities.models import *
from django.http.response import HttpResponse


# rom rest_framework.views import APIView
# REST API for Django
def __main__():
    pass


def index(request):
    if request.method == 'POST':
        pass
    print("index request")
    print(request.body)
    q = Question(question_text="who's fist?", pub_date=timezone.now())
    q.save()

    # for u in User.objects.all():
    #     print(f'type: {u.type} \tUsername: {u.name}')
    return HttpResponse(200)