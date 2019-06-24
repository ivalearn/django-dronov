from django.http import HttpRequest, HttpResponse, Http404
from .models import Category, Good
#from django.shortcuts import render


def index(req: HttpRequest, cat_id: int = None) -> HttpResponse:
    try:
        if cat_id is None:
            cat = Category.objects.first()
        else:
            cat = Category.objects.get(pk=cat_id)
    except Category.DoesNotExist:
        raise Http404
    goods = Good.objects.filter(category=cat)
    s = f"Категория: {cat.name} <br><br>"
    for good in goods:
        s += f"({good.pk}) {good.name}<br>"
    return HttpResponse(s)


def good(req: HttpRequest, good_id: int) -> HttpResponse:
    try:
        good = Good.objects.get(pk=good_id)
    except Good.DoesNotExist:
        raise Http404
    s = f"{good.name}<br><br>{good.category.name}<br><bt>{good.description}"
    if not good.in_stock:
        s += "<br><br>нет в наличии!"
    return HttpResponse(s)
