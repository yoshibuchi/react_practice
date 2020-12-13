from django.urls import path

from .views import SpaAPIView


urlpatterns = [
    path('', SpaAPIView.as_view()),
]