from django.conf.urls import patterns, include, url
from .views import SignUp

urlpatterns = patterns('',
    url(r'^signup/$', SignUp.as_view(), name='signup'),
)
