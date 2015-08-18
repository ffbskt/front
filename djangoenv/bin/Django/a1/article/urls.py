__author__ = 'denis'
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^1/', 'article.views.basic_one'),
    url(r'^2/', 'article.views.template_2'),
    url(r'^3/', 'article.views.template_3'),
    url(r'^articles/all/$', 'article.views.articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^', 'article.views.articles'),
    ]