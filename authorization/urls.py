from django.conf.urls import url
from authorization import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^add/$', views.add_user_to_db, name='add'),
    url(r'^check_user/$', views.check_user, name='check_user')
]
