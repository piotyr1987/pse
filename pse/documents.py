from django_elasticsearch_dsl import DocType, Index

from pse.models import Package

search_index = Index('package')
search_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@search_index.doc_type
class PackageDocument(DocType):

    class Meta:
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
