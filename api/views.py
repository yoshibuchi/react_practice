from rest_framework import generics

from books.models import Spa
from .serializers import SpaSerializer


class SpaAPIView(generics.ListAPIView):
    queryset = Spa.objects.all()
    serializer_class = SpaSerializer