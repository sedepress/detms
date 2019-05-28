from django.urls import re_path
from tms import views

app_name = 'tms'
urlpatterns = [
    re_path(r'^login/$', views.user_login, name='login'),
    re_path(r'^welcome/$', views.welcome, name='welcome'),
    re_path(r'^logout/$', views.user_logout, name='logout'),
    re_path(r'^user_list/$', views.user_list, name='user_list'),
    re_path(r'^line/index/$', views.line_index, name='line_index'),
    re_path(r'^line/store/$', views.line_store, name='line_store'),
    re_path(r'^line/(?P<line_id>[\d]+)/update/$', views.line_update, name='line_update'),
    re_path(r'^line/(?P<line_id>[\d]+)/delete/$', views.line_delete, name='line_delete'),
    re_path(r'^consignment/index/$', views.consignment_index, name='consignment_index'),
    re_path(r'^consignment/store/$', views.consignment_store, name='consignment_store'),
]