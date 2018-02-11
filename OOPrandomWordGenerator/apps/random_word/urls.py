from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  url(r'^randomword/reset$', views.reset),
  url(r'^randomword/generate$', views.index), #no trailing slash from a post request.
  url(r'^randomword/$', views.index)     # This line has changed!
]

