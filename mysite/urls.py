"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from polls import views

# 고정 url: http://localhost:8000/
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('polls/', views.index, name='index')
    path('polls/', include('polls.urls')) # 이 링크에 대한 모든 내용은 작업 위임 (include: 다른 url configuration을 다른 파일로 전달해)
]
