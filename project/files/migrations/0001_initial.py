# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import admin_resumable.fields
import uuid
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileToken',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=False)),
                ('token', shortuuidfield.fields.ShortUUIDField(max_length=22, blank=True, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SharedFile',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=False)),
                ('short_id', shortuuidfield.fields.ShortUUIDField(max_length=22, blank=True, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('file', admin_resumable.fields.ModelAdminResumableFileField(upload_to='unused')),
                ('hotlink', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='filetoken',
            name='file',
            field=models.ForeignKey(to='files.SharedFile', related_name='tokens'),
        ),
    ]
