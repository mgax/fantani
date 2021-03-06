from django.conf.urls import include, url
from django.contrib import admin
from campaign import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^_crashme$', views.crashme, name='crashme'),
    url(r'^$', views.index),
    url(r'^submit$', views.submit, name='submit'),
    url(r'^overview$', views.overview, name='overview'),
]
