"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from app import views

urlpatterns = [
    # 設定 url 路徑 與 要使用的 function， Django 的根目錄預設不用寫
    # path("", views.hello),
    path("hello/", views.hello),
    path("lotto/", views.lotto),
    path("", include("todo.urls")),
    path("user/", include("user.urls")),
    path("admin/", admin.site.urls),
]
