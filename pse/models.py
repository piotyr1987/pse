from django.db import models


class Package(models.Model):
    name = models.CharField(verbose_name='Tytuł pakietu', max_length=250)
    author = models.CharField(verbose_name='Autor', max_length=250)
    description = models.TextField(verbose_name='Opis pakietu')
    keywords = models.CharField(verbose_name='Słowa kluczowe', max_length=250, null=True, blank=True)
    version = models.CharField(verbose_name='Bieżąca wersja', max_length=50)
    url = models.URLField(verbose_name='Url do projektu', max_length=200, unique=True)

    def __str__(self):
        return self.name
