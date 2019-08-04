from django.urls import path, re_path
from . import views,views_cbv

app_name = 'dojo'
urlpatterns = [
    re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum, name='mysum'),
    re_path(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello, name='hello'),
    path('list1/', views.post_list1, name='post_list1'),
    path('list2/', views.post_list2, name='post_list2'),
    path('list3/', views.post_list3, name='post_list3'),
    path('excel/', views.excel_download, name='excel_download'),

    path('cbv/list1/', views_cbv.post_list1, name='post_list1'),
    path('cbv/list2/', views_cbv.post_list2, name='post_list2'),
    path('cbv/list3/', views_cbv.post_list3, name='post_list3'),
    path('cbv/excel/', views_cbv.excel_download, name='excel_download'),

    path('new/', views.post_new, name='post_new'),
    path('<int:id>/edit/', views.post_edit, name='post_edit'),
    path('<int:id>/', views.post_detail, name='post_detail'),

]
