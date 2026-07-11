from django.test import TestCase
from django.urls import reverse
from .models import SGC, Project

class MELCoreTests(TestCase):
    def setUp(self):
        self.sgc = SGC.objects.create(name="Test SGC", country="Test Country")
        self.project = Project.objects.create(sgc=self.sgc, title="Test Project")

    def test_sgc_creation(self):
        self.assertEqual(SGC.objects.count(), 1)
        self.assertEqual(SGC.objects.first().name, "Test SGC")

    def test_project_creation(self):
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.first().title, "Test Project")

    def test_dashboard_view(self):
        response = self.client.get(reverse('mel_core:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "SGCI MEL Dashboard")
        self.assertContains(response, "Total SGCs")
