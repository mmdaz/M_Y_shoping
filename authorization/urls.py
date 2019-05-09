from django.conf.urls import url
from authorization import views

urlpatterns = [
    url(r'^register/$', views.register, name='register')
]
