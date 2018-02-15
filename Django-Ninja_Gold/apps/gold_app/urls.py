from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  url(r'^reset$', views.reset),
  url(r'^process$', views.process),
  url(r'^process/(?P<place>\w+)$', views.process_param),
  url(r'^$', views.index)     # This line has changed!
]
