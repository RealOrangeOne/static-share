from django.db import models
import uuid
from admin_resumable.fields import ModelAdminResumableFileField
from shortuuidfield import ShortUUIDField
from datetime import timedelta
from django.core.urlresolvers import reverse
import os.path
from django.conf import settings


class SharedFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    short_id = ShortUUIDField()
    created = models.DateTimeField(auto_now_add=True)
    file = ModelAdminResumableFileField()
    hotlink = models.BooleanField(default=False)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.get_original_filename()

    def get_original_filename(self):
        return "_".join(self.file.name.split('_')[1:])

    def get_absolute_url(self):
        return reverse('files:file', args=(self.short_id,))

    def get_type_image(self):
        extension = self.get_original_filename().split('.')[-1]
        icon_file = os.path.join(settings.STATICFILES_DIRS[0], 'img', 'icons', "{0}.png".format(extension))
        filename = extension if os.path.exists(icon_file) else "_page"
        return os.path.join(settings.STATIC_URL, 'img', 'icons', "{0}.png".format(filename))


class FileToken(models.Model):
    valid_time = timedelta(minutes=5)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    token = ShortUUIDField()
    file = models.ForeignKey(SharedFile, null=False, blank=False, related_name="tokens")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Token for {0} created at {1}".format(self.file.file.name, self.created)
