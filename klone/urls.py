"""klone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from klone import views

urlpatterns = [
    url(r'^$', views.question_list),
    url(r'^create/', views.question_create),
    url(r'^admin/', admin.site.urls),
    url(r'^mimi/', views.hello_world),
    url(r'^question/delete/(?P<question_id>\d+)/$',views.delete_question, name='delete'),
    url(r'^question/(?P<question_id>\d+)/status/(?P<status_name>\S+)/change/$', views.change_status, name="change_status"),
    url(r'^question/(?P<question_id>\d+)/$', views.question_detail, name='question_detail')

]
