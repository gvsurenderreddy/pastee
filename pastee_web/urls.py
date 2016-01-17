from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^paste/view/(?P<paste_name>\w{6})/$', views.view_paste, name='view_paste'),
    url(r'^paste/add/$', views.add_paste, name='add_paste')
]
