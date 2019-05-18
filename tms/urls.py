from django.urls import re_path
from tms import views

app_name = 'tms'
urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path('^welcome/$', views.welcome, name='welcome'),
]