from django.contrib import admin
from django.conf.urls import url,include
from.import views
urlpatterns=[
    url('',views.home,name='home'),
    url(r'^place/(?P<name>.+?)/$', views.place, name="place"),
]
