from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from project.files.views import uploaded_file

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_resumable/', include('admin_resumable.urls')),
    url(r'^files/', include('project.files.urls', namespace="files")),
    url(r'^uploads/(?P<filename>.*)', uploaded_file, name="upload"),
    url(r'', include("project.pages.urls", namespace="pages"))
]


urlpatterns += staticfiles_urlpatterns()
