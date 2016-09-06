from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>.*)/hot/$', views.hotlink_file_download, name="file_hot"),
    url(r'^(?P<id>.*)/(?P<token>.*)/$', views.file_download, name="file_download"),
    url(r'^(?P<id>.*)/$', views.SharedFileDetails.as_view(), name="file"),
]
