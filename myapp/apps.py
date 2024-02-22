from django.apps import AppConfig

# define INSTALLED_APPS config path.
# cmd line run : ython manage.py makemigrations myapp
# 再次运行 python manage.py migrate 命令，在数据库里创建新定义的模型的数据表：


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
