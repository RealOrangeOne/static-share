from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import SharedFile, FileToken
import datetime
from django.utils import timezone


class SharedFileDetails(TemplateView):
    template_name = "file.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['file'] = get_object_or_404(SharedFile, short_id=kwargs['id'])
        context['token'] = FileToken.objects.create(file=context['file'])
        return context


def file_download(request, token, id):
    time_threshold = timezone.now() - FileToken.valid_time
    FileToken.objects.filter(created__lt=time_threshold)
    file = get_object_or_404(SharedFile, short_id=id)
    token = get_object_or_404(FileToken, token=token, file=file)
    token.delete()  # delete after used
    return HttpResponse(file.file.name)
