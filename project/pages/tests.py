from django.core.urlresolvers import reverse
from django.test import TestCase


class IndexPageTestCase(TestCase):
    def test_accessable(self):
        response = self.client.get(reverse("pages:index"))
        self.assertEqual(response.status_code, 200)
