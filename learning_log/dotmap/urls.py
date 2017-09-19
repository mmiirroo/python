from django.conf.urls import url       

from . import views

urlpatterns = [
    url(r'^address/$', views.address, name='address'),
]
