from django.http import Http404
from .models import Category, Good
from django.views.generic import ListView, TemplateView


class GoodListView(ListView):
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
        context['cats'] = Category.objects.all().order_by('name')
        context['category'] = self._cat
        return context


class GoodDetailView(TemplateView):
    template_name = 'good.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['good'] = Good.objects.get(pk=self.kwargs['good_id'])
        except Good.DoesNotExist:
            raise Http404
        context['cats'] = Category.objects.all().order_by('name')
        context['cat_page'] = self.request.GET.get('cat_page', '1')
        return context
