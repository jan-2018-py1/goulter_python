from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  url(r'^amadon/clear/$',views.clear),
  url(r'^amadon/checkout$',views.checkout),
  url(r'^amadon/buy/$', views.buy),
  url(r'^amadon/$', views.index)     # This line has changed!
]
