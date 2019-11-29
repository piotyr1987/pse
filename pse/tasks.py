import requests

from pse.celery import app
from pse.models import Package


@app.task
def import_package(url):
    res = requests.get(url)
    if res.status_code != 200:
        return
    result = res.json()
    try:
        obj = Package.objects.get(url=result['info']['project_url'])
    except Package.DoesNotExist:
        Package.objects.create(
            name=result['info']['name'],
            url=result['info']['project_url'],
            author=result['info']['author'],
            author_email=result['info']['author_email'],
            description=result['info']['description'],
            keywords=result['info']['keywords'],
            version=result['info']['version'],
        )
    else:
        obj.name = result['info']['name']
        obj.author = result['info']['author']
        obj.author_email = result['info']['author_email']
        obj.description = result['info']['description']
        obj.keywords = result['info']['keywords']
        obj.version = result['info']['version']
        obj.save()
