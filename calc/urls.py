from django.conf.urls import url

from . import views

app_name = 'calc'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^boot_submit/$', views.boot_submit, name='boot_submit'),
    url(r'^generic_index/$', views.IndexView.as_view(), name='generic_index'),
]
