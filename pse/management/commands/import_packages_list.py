import feedparser
import os
from urllib.parse import urlparse

from django.core.management.base import BaseCommand
from pse.tasks import import_package

PYPI_URL = 'https://pypi.org/rss/packages.xml'


class Command(BaseCommand):
    help = """Import packages from pypi.org."""

    def get_url_list(self):
        url_list = []
        for item in feedparser.parse(PYPI_URL).entries:
            link = list(filter(None, urlparse(item['link']).path.split(os.sep)))[-1]
            url_list.append('https://pypi.org/pypi/{}/json'.format(link))
        return url_list

    def handle(self, *args, **options):
        for url in self.get_url_list():
            import_package.delay(url)
