from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from pse.models import Package


@registry.register_document
class PackageDocument(Document):
    class Index:
        name = 'package'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Package

        fields = [
            'id',
            'name',
            'author',
            'author_email',
            'description',
            'version',
            'url',
            'keywords',
        ]
