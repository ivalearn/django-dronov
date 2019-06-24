from django.http import HttpRequest, HttpResponse, Http404
from .models import Category, Good
from django.shortcuts import render


def index(req: HttpRequest, cat_id: int = None) -> HttpResponse:
    cats = Category.objects.all().order_by('name')
    try:
        if cat_id is None:
            cat = Category.objects.first()
        else:
            cat = Category.objects.get(pk=cat_id)
    except Category.DoesNotExist:
        raise Http404
    goods = Good.objects.filter(category=cat)
    return render(req, 'index.html', {
        'category': cat,
        'cats': cats,
        'goods': goods,
    })


def good(req: HttpRequest, good_id: int) -> HttpResponse:
    try:
        good = Good.objects.get(pk=good_id)
    except Good.DoesNotExist:
        raise Http404
    return render(req, 'good.html', {'good': good})
