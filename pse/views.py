from django.shortcuts import render
from pse.documents import PackageDocument


def search(request):
    q = request.GET.get('q', '')

    result = PackageDocument.search().query('multi_match', query=q, fields=[
        'name',
        'author',
        'version',
        'author_email',
        'description',
        'keywords',
    ])

    return render(request, 'pse/search.html', {'object_list': result.execute()})
