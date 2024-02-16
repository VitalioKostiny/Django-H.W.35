from django.urls import path
from . import views
# Префикс /cards/
urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:card_id>/', views.get_card_by_id, name='card'),
    path('catalog/<slug:slug>/', views.get_category_by_name, name='category'),
]
