from django.db import models
import os
import uuid
from admin_resumable.fields import ModelAdminResumableFileField
from shortuuidfield import ShortUUIDField


def build_save_path(obj, filename):
    return obj.get_save_path(filename)


class SharedFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    short_id = ShortUUIDField()
    created = models.DateTimeField(auto_now_add=True)
    file = ModelAdminResumableFileField(upload_to=build_save_path)
    hotlink = models.BooleanField(default=False)
    published = models.BooleanField(default=True)

    filename = ""

    def get_save_path(self, filename):
        self.filename = filename
        return os.path.join(str(self.id), str(self.short_id), filename)

    def get_private_path(self):
        return self.get_save_path(self.filename)

    def get_original_filename(self):
        return "_".join(self.file.name.split('_')[1:])
