import mock
from django.core.paginator import PageNotAnInteger
from django.http import Http404
from django.test import RequestFactory, TestCase

from pse.factories import PackageFactory
from pse.views import (
    ApiSearchView,
    BaseView,
    SearchView,
)


class BaseViewTest(TestCase):

    def setUp(self):
        self._package = PackageFactory.create(id=123, name='test')
        self._view = BaseView()

    @mock.patch('pse.views.Paginator')
    @mock.patch('pse.views.PackageDocument')
    def test_should_return_paginator(self, package_document, paginator):
        page = 1
        q = 'test'
        pagi = paginator([], 2)
        pagi.page.return_value = page
        package_document.search.query.return_value = self._package

        result = self._view.get_search_results(q, page)

        self.assertEqual(result, pagi.page(page))

    @mock.patch('pse.views.Paginator')
    @mock.patch('pse.views.PackageDocument')
    def test_should_return_http404(self, package_document, paginator):
        page = 3
        q = 'test'
        pagi = paginator([], 2)
        pagi.page.side_effect = PageNotAnInteger
        with self.assertRaises(Http404):
            self._view.get_search_results(q, page)


class SearchViewTestCase(TestCase):
    def setUp(self):
        self._view = SearchView

    @mock.patch('pse.views.PackageDocument')
    @mock.patch('pse.views.SearchView.get_search_results')
    def test_should_return_render_template(self, mock_search_results, package_document):
        request = RequestFactory().get('/')
        view = self._view.as_view()

        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'pse/search.html')


class ApiSearchViewTestCase(TestCase):
    def setUp(self):
        self._view = ApiSearchView

    @mock.patch('pse.views.PackageDocument')
    @mock.patch('pse.views.ApiSearchView.get_search_results')
    def test_should_return_empty_json(self, mock_search_results, package_document):
        request = RequestFactory().get('/api')
        view = self._view.as_view()

        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {})

    @mock.patch('pse.views.PackageDocument')
    @mock.patch('pse.views.ApiSearchView.get_search_results')
    def test_should_return_json(self, mock_search_results, package_document):
        expected = {
            "name": {
                "name": "name",
                "author": "author",
                "author_email": "author_email@test.pl",
                "description": "description",
                "version": "1.0.0.2",
                "keywords": "klucz",
            },
        }
        object_list = PackageFactory.create_batch(
            1,
            name="name",
            author="author",
            author_email="author_email@test.pl",
            description="description",
            version="1.0.0.2",
            keywords="klucz",
        )
        mock_search_results.return_value = object_list
        request = RequestFactory().get('/api')
        view = self._view.as_view()

        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, expected)
