from django.db import models
import os
import uuid
from admin_resumable.fields import ModelAdminResumableFileField
from shortuuidfield import ShortUUIDField
from datetime import timedelta


class SharedFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    short_id = ShortUUIDField()
    created = models.DateTimeField(auto_now_add=True)
    file = ModelAdminResumableFileField()
    hotlink = models.BooleanField(default=False)
    published = models.BooleanField(default=True)

    def get_original_filename(self):
        return "_".join(self.file.name.split('_')[1:])


class FileToken(models.Model):
    valid_time = timedelta(minutes=5)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    token = ShortUUIDField()
    file = models.ForeignKey(SharedFile, null=False, blank=False, related_name="tokens")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Token for {0} created at {1}".format(self.file.file.name, self.created)
