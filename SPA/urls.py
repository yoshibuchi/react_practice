from django.urls import path
from .views import SpaListView


urlpatterns = [
    path('', SpaListView.as_view(), name='home')
]