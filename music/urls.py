from django.contrib import admin
from django.urls import path, include

# 导入views文件
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/music/index
    path('index', views.index_view)
]
