from django.urls import path
from .views import GoodListView, GoodDetailView

urlpatterns = [
    path('', GoodListView.as_view(), name='index'),
    path('<int:cat_id>/', GoodListView.as_view(), name='index'),
    path('good/<int:good_id>/', GoodDetailView.as_view(), name='good'),
]
