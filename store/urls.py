from django.urls import path
from .views import store
from .views import product_detail
from .views import search
from .views import submit_review
from .views import search_suggestions

urlpatterns = [
    path('', store, name='store'),
    path('category/<slug:category_slug>/', store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', product_detail, name='product_detail'),
    path('search/', search, name='search'),
    path('search_suggestions/', search_suggestions, name='search_suggestions'),
    path('submit_review/<int:product_id>/', submit_review, name='submit_review'),
]