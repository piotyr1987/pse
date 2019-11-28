from django.conf import settings
from django.core.paginator import (
    EmptyPage,
    PageNotAnInteger,
    Paginator,
)
from django.http import Http404, JsonResponse
from django.views.generic import View, TemplateView

from pse.documents import PackageDocument


class BaseView(View):

    def get_search_results(self, q, page):
        result = PackageDocument.search().query('multi_match', query=q, fields=[
            'name',
            'author',
            'version',
            'author_email',
            'description',
            'keywords',
        ])
        p = Paginator(result.execute(), settings.PAGINATION_PAGE_SIZE)

        try:
            return p.page(page)
        except (EmptyPage, PageNotAnInteger):
            raise Http404


class SearchView(TemplateView, BaseView):
    template_name = "pse/search.html"

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        page = request.GET.get('page', 1)
        object_list = self.get_search_results(q, page)
        return self.render_to_response({'object_list': object_list})


class ApiSearchView(BaseView):

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        page = request.GET.get('page', 1)
        object_list = self.get_search_results(q, page)

        context = {}
        for item in object_list:
            context[item.name] = {
                'name': item.name,
                'author': item.author,
                'author_email': item.author_email,
                'description': item.description,
                'version': item.version,
                'keywords': item.keywords,
            }
        return JsonResponse(context)
