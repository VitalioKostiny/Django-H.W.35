from django.contrib import admin
from django.urls import path, include
from cards import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('cards/', include('cards.urls')),
]


