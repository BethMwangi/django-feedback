"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib.auth import views
from django.contrib import admin
from login.views import *
from login.forms import LoginForm
 
urlpatterns =[ 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.login, name='login'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^accounts/login/$', views.login, name= 'login'), # If user is not login it will redirect to login page
    url(r'^register/$', register, name='register'),
    url(r'^register/success/$', register_success, name='register_success'),
    url(r'^home/$', home, name='home'),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),


]