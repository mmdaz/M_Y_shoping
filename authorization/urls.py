from django.conf.urls import url
from authorization import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^add/$', views.add, name='add'),


]
