from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^boot_submit/$', views.boot_submit, name='boot_submit'),
]
