from django.views.generic import ListView
from .models import Spa


class SpaListView(ListView):
    model = Spa
    template_name = 'Spa_list.html'