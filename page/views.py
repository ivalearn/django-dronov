from django.http import Http404
from .models import Category, Good
from django.core.paginator import Paginator, InvalidPage
from django.views.generic import TemplateView


class GoodListView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all().order_by('name')
        try:
            if 'cat_id' in self.kwargs:
                cat = Category.objects.get(pk=self.kwargs['cat_id'])
            else:
                cat = Category.objects.first()
        except Category.DoesNotExist:
            raise Http404
        context['category'] = cat
        page_no = self.request.GET.get('page')
        all_goods = Good.objects.filter(category=cat)
        paginator = Paginator(all_goods, 2)
        try:
            context['goods'] = paginator.page(page_no)
        except InvalidPage:
            context['goods'] = paginator.page(1)
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
