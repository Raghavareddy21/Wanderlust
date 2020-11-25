from django.contrib import admin
from django.conf.urls import url,include
from.import views
urlpatterns=[
    url(r'^home/$',views.home,name='home'),
    url(r'^place/$', views.place, name="place"),
    url(r'^login/$',views.login,name='login.html'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^profile/$',views.profileView,name='signup'),
    url(r'^logout/$',views.logoutView,name='logout.html'),
]
