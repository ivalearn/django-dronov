from django.http import Http404
from .models import Category, Good
from django.views.generic import ListView, DetailView
from django.views.generic.base import ContextMixin


class CategoryListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all().order_by('name')
        return context


class GoodListView(ListView, ContextMixin):
    template_name = 'index.html'
    paginate_by = 2

    def get_queryset(self):
        try:
            if 'cat_id' in self.kwargs:
                self._cat = Category.objects.get(pk=self.kwargs['cat_id'])
            else:
                self._cat = Category.objects.first()
        except Category.DoesNotExist:
            raise Http404
        return Good.objects.filter(category=self._cat).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self._cat
        return context


class GoodDetailView(DetailView, ContextMixin):
    template_name = 'good.html'
    model = Good
    pk_url_kwarg = 'good_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_page'] = self.request.GET.get('cat_page', '1')
        return context
