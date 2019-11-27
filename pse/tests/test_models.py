from django.test import TestCase
from pse.factories import PackageFactory
from pse.models import Package


class PackageTestCase(TestCase):
    def setUp(self):
        self._pk = 102
        self._package = PackageFactory.create(pk=self._pk, name='test')

    def test_should_return_title(self):
        result = Package.objects.get(pk=self._pk)

        self.assertEqual(result.__str__(), 'test')
