import factory
from pse.models import Package


class PackageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Package

    name = factory.Sequence(lambda i: 'name{}'.format(i))
    author = factory.Sequence(lambda i: 'author{}'.format(i))
    author_email = factory.Sequence(lambda i: 'author_email{}@test.pl'.format(i))
    description = factory.Sequence(lambda i: 'description{}'.format(i))
    version = factory.Sequence(lambda i: '1.0.0.{}'.format(i))
    url = factory.Sequence(lambda i: 'https://test{}.pl'.format(i))
