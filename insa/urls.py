"""insa URL Configuration

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
from insa_record import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^insa_record/insert/$', views.insert, name='insert'),
    url(r'^insa_record/list/$', views.list, name='list'),
    url(r'^insa_record/detail/(?P<detail_id>\d+)/$', views.detail, name='detail'),
    url(r'^insa_record/print_page/(?P<detail_id>\d+)/$', views.print_page, name='print_page'),
    url(r'^insa_record/$', views.mainpage, name='main'),
    url(r'^admin/', include(admin.site.urls)),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
