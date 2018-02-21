from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  url(r'^courses/dodestroy/(?P<uid>\d+)/$', views.dodestroy),
  url(r'^courses/destroy/(?P<uid>\d+)/$', views.destroy_check),
  url(r'^create/$', views.create),
  url(r'^$', views.index)     # This line has changed!
]
