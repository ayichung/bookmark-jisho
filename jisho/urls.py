from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='jisho-home'),
    path('search/<query>', views.search, name='jisho-search'),
]