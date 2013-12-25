from django.conf.urls import patterns, url
from .views import SignUp

urlpatterns = patterns('',
    url(r'^signup/$', SignUp.as_view(), name='signup'),
)
