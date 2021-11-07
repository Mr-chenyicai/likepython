"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# 静态文件服务
from django.conf.urls.static import static
from sales.views import listorders

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sales/', include('sales.urls')), # 凡是以sales开头的就以 incloud指定的那张表去找  这里为一级路由，去找到对应的二级路由（建的app例如sales）访问
    path('api/mgr/', include('mgr.urls')),
] + static("/", document_root="./z_dist")
