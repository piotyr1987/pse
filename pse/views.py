from django.core.paginator import (
    EmptyPage,
    PageNotAnInteger,
    Paginator,
)
from django.http import Http404
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
    p = Paginator(result.execute(), 2)

    page = request.GET.get('page', 1)
    try:
        object_list = p.page(page)
    except (EmptyPage, PageNotAnInteger):
        raise Http404
    return render(request, 'pse/search.html', {'object_list': object_list})
