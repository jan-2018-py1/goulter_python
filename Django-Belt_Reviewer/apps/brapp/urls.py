from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  # url(r'^books/(?P<bookid>\d+)/$', views.bookwall),
  url(r'^logout$', views.logout),
  url(r'^delete_review/(?P<rid>\d+)/(?P<bookid>\d+)/$', views.delete_review),
  url(r'^user/(?P<uid>\d+)/$', views.users),
  url(r'^books/processreview/(?P<bookid>\d+)/$', views.processreview),
  url(r'^books/processbook/$', views.processbook),
  url(r'^books/(?P<bookid>\d+)/$', views.bookwall),
  url(r'^books/add$', views.getabook),
  url(r'^books$', views.books),
  url(r'^login$', views.login),
  url(r'^registered$', views.registered),
  url(r'^doregister$', views.doregister),
  url(r'^$', views.index)     # This line has changed!
]
