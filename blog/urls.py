from django.urls import path, re_path
from . import views, views_cbv

app_name = 'blog' #프로젝트 레벨에서 namesapce 지정 후 app_name 지정 필요함
urlpatterns = [
    path('', views_cbv.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
    path('<int:id>/edit/', views.post_edit, name='post_edit'),

    path('cbv/new/', views_cbv.post_new),
]
