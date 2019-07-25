"""practice1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect

# def root(request):
#     return redirect('blog:post_list')

urlpatterns = [
    path('', lambda r:redirect('blog:post_list'), name='root'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('dojo/', include('dojo.urls', namespace='dojo')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('shop/', include('shop.urls', namespace='shop')),
    #namespace 지정 후 각각의 urls.py에서 app_name도 지정해주어야 함
    #name이 중복되는 경우를 대비해 namespace가 필요함
]

if settings.DEBUG: #html 페이지에 body 태그를 써야 함
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]


