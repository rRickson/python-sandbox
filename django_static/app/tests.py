import os
from django.test import TestCase, override_settings
from django.conf import settings
from django.contrib.staticfiles import finders

class StaticFilesTestCase(TestCase):

    def test_static_files_settings(self):
        self.assertEqual(settings.STATIC_URL, '/static/')
        self.assertIn(os.path.join(settings.BASE_DIR, 'static'), settings.STATICFILES_DIRS)
        self.assertEqual(settings.STATIC_ROOT, os.path.join(settings.BASE_DIR, 'staticfiles'))

    def test_static_file_finder(self):
        result = finders.find('styles.css')
        self.assertIsNotNone(result)
        self.assertTrue(result.endswith('styles.css'))
