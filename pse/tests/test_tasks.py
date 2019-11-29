import json
import mock

from django.test import TestCase

from pse.factories import PackageFactory
from pse.models import Package
from pse.tasks import import_package
from pse.tests.fake_data import fake_data


class ImportPackageTestCase(TestCase):

    def setUp(self):
        self._author = 'Pivot Horizon'
        self._url = 'https://pypi.org/project/leo-python/'

    def _fake_response(self, url):
        response_mock = mock.Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = json.loads(fake_data)
        return response_mock

    def _no_content_response(self, url):
        response_mock = mock.Mock()
        response_mock.status_code = 204
        return response_mock

    @mock.patch('pse.tasks.requests')
    def test_should_check_author_has_added(self, mock_requests):
        mock_requests.get.side_effect = self._fake_response
        import_package('http://test.pl')

        result = Package.objects.get(author=self._author)

        self.assertEqual(result.author, self._author)

    @mock.patch('pse.tasks.requests')
    def test_should_check_author_has_update(self, mock_requests):
        self._package = PackageFactory.create(author='test', url=self._url)
        mock_requests.get.side_effect = self._fake_response
        import_package('http://test.pl')

        result = Package.objects.get(url=self._url)

        self.assertEqual(result.author, self._author)

    @mock.patch('pse.tasks.requests')
    def test_should_return_if_not_status_code_200(self, mock_requests):
        mock_requests.get.side_effect = self._no_content_response
        result = import_package(self._url)

        self.assertFalse(result)
