from django.http import HttpRequest, HttpResponse, Http404
from .models import Category, Good
from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage


def index(req: HttpRequest, cat_id: int = None) -> HttpResponse:
    cats = Category.objects.all().order_by('name')
    try:
        if cat_id is None:
            cat = Category.objects.first()
        else:
            cat = Category.objects.get(pk=cat_id)
    except Category.DoesNotExist:
        raise Http404
    page_no = req.GET.get('page')
    all_goods = Good.objects.filter(category=cat)
    paginator = Paginator(all_goods, 2)
    try:
        goods = paginator.page(page_no)
    except InvalidPage:
        goods = paginator.page(1)
    return render(req, 'index.html', {
        'category': cat,
        'cats': cats,
        'goods': goods,
    })


def good(req: HttpRequest, good_id: int) -> HttpResponse:
    cats = Category.objects.all().order_by('name')
    try:
        good = Good.objects.get(pk=good_id)
    except Good.DoesNotExist:
        raise Http404
    return render(req, 'good.html', {
        'good': good,
        'cats': cats,
        'cat_page': req.GET.get('cat_page', '1')
    })
