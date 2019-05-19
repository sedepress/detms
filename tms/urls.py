from django.urls import re_path
from tms import views

app_name = 'tms'
urlpatterns = [
    re_path(r'^login/$', views.user_login, name='login'),
    re_path(r'^welcome/$', views.welcome, name='welcome'),
    re_path(r'^logout/$', views.user_logout, name='logout'),
    re_path(r'^user_list/$', views.user_list, name='user_list'),
]