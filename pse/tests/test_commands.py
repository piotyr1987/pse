import mock
from django.test import TestCase
from pse.management.commands.import_packages_list import Command


class CommandImportPackagesListTestCase(TestCase):

    def setUp(self):
        self._command = Command()
        self._author = 'Pivot Horizon'
        self._url = 'https://pypi.org/project/leo-python/'

    @mock.patch('pse.management.commands.import_packages_list.feedparser')
    def test_should_return_list_with_urls(self, mock_feedparser):
        expected = ['https://pypi.org/pypi/easyjaeger/json', 'https://pypi.org/pypi/kgd/json']
        pypi_data = {
            'entries': [
                {
                    'link': 'https://pypi.org/pypi/easyjaeger/'
                },
                {
                    'link': 'https://pypi.org/pypi/kgd/'
                }
            ]
        }
        mock_feedparser.parse.return_value = pypi_data

        url_list = self._command.get_url_list()

        self.assertEqual(url_list, expected)
