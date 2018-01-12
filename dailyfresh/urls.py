"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('apps.user', namespace='user')),     # 配置用户路由
    url(r'^order/', include('apps.order', namespace='order')),      # 配置订单路由
    url(r'^cart/', include('apps.cart', namespace='cart')),     # 配置购物路由
    url(r'^', include('apps.goods', namespace='goods')),    # 配置商品路由
    url(r'^tinymce/', include('tinymce.urls')),     # 配置富文本编辑器路由
]
