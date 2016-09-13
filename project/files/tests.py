from django.test import TestCase
from model_mommy import mommy
from .models import SharedFile
from django.core.files.uploadedfile import SimpleUploadedFile


class SharedFileTestCase(TestCase):
    def setUp(self):
        asset = SimpleUploadedFile(
            name='902598_test_file.txt',
            content='',
            content_type='text/plain'
        )
        self.file = mommy.make(SharedFile, file=asset)

    def test_str(self):
        self.assertEqual(str(self.file), self.file.get_original_filename())

    def test_get_original_filename(self):
        self.assertIn('test_file', self.file.get_original_filename())

    def test_absolute_url(self):
        self.assertEqual(self.file.get_absolute_url(), '/files/{0}/'.format(self.file.short_id))
