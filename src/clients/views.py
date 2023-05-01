from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from clients.models import Client


class ListClientView(LoginRequiredMixin, ListView):
    queryset = Client.objects.all()
    template_name = 'clients/list.html'
