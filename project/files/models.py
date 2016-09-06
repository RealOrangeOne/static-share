from django.db import models
import uuid
from admin_resumable.fields import ModelAdminResumableFileField
from shortuuidfield import ShortUUIDField
from datetime import timedelta
from django.core.urlresolvers import reverse


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


class FileToken(models.Model):
    valid_time = timedelta(minutes=5)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    token = ShortUUIDField()
    file = models.ForeignKey(SharedFile, null=False, blank=False, related_name="tokens")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Token for {0} created at {1}".format(self.file.file.name, self.created)
