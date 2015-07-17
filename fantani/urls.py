from django.conf.urls import include, url
from django.contrib import admin
from campaign import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^submit$', views.submit, name='submit'),
]
