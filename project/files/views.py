from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import SharedFile, FileToken
import mimetypes
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


mimetypes.init()


class SharedFileDetails(TemplateView):
    template_name = "file.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['file'] = get_object_or_404(SharedFile, short_id=kwargs['id'])
        context['token'] = FileToken.objects.create(file=context['file'])
        return context


def FileResponse(file):
    response = HttpResponse(file.file)
    response['Content-Type'] = mimetypes.guess_type(file.get_original_filename())[0]
    response['Content-Disposition'] = 'attachment; filename="{0}"'.format(file.get_original_filename())
    return response


def file_download(request, id, token):
    time_threshold = timezone.now() - FileToken.valid_time
    FileToken.objects.filter(created__lt=time_threshold)
    file = get_object_or_404(SharedFile, short_id=id, published=True)
    token = get_object_or_404(FileToken, token=token, file=file)
    token.delete()  # delete after used
    return FileResponse(file)


def hotlink_file_download(request, id):
    file = get_object_or_404(SharedFile, short_id=id, hotlink=True, published=True)
    return FileResponse(file)


@login_required
def uploaded_file(request, filename):
    file = get_object_or_404(SharedFile, file=request.get_full_path()[1:])  # strip preceding slash
    response = FileResponse(file)
    del response['Content-Disposition']
    return response
