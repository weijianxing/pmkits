#-*- coding: utf-8 -*-
# 
# __author__ : jianxing.wei
# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()


# 启动 server python manage.py runserver 8080 or python manage.py runserver localhosts:8081

from  pmmonkey.entities.models import *

# for u in User.objects.all():
#     print(f'type: {u.type} \tUsername: {u.name}')
