from django.conf.urls import url

from . import views

app_name = 'calc'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='generic_index'),
    url(r'^boot_submit/$', views.boot_submit, name='boot_submit'),
]
