from django.urls import path, re_path
from AppTow import views

app_name = 'AppTow'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'/formpage', views.form_name_view, name='form_name'),
    re_path(r'/topics', views.topics, name='new_topic'),
    re_path(r'/index1/$', views.index1, name='index1'),
    re_path(r'/relative/$', views.relative, name='relative'),
    re_path(r'/other/$', views.other, name='other'),
    re_path(r'/index2/', views.index2, name='index2'),
    re_path(r'/register/', views.register, name='register'),
    re_path(r'/user_login/$', views.user_login, name='user_login'),
]
