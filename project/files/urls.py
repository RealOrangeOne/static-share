from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<token>.*)/(?P<id>.*)/$', views.file_download, name="file_download"),
    url(r'^(?P<id>.*)/$', views.SharedFileDetails.as_view(), name="file"),
]
