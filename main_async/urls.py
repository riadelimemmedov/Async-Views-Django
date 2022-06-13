"""main_async URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('smoke_some_meats/',smoke_some_meats,name='smoke_some_meats'),
    path('burn_some_meats/',burn_some_meats,name='burn_some_meats'),
    path('sycn_to_asycn/',async_with_sync_view,name='async_with_sync_view'),
    path('async/',async_view,name='async_view'),
    path('sync/',sync_view,name='sync_view'),
    path('',index,name='index')
]
