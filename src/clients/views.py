from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .forms import CreateClientForm
from .models import Client


class ListClientView(LoginRequiredMixin, ListView):
    queryset = Client.objects.all()
    template_name = 'clients/list.html'


class CreateClientView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Client
    form_class = CreateClientForm
    template_name = 'clients/create.html'
    success_message = 'Клиент успешно добавлен'
    success_url = reverse_lazy('clients:list')


class DetailClientView(LoginRequiredMixin, SuccessMessageMixin, UpdateView, DetailView):
    model = Client
    form_class = CreateClientForm
    template_name = 'clients/detail.html'
    success_message = 'Клиент успешно сохранен'
    
    def get_success_url(self):
        return reverse_lazy('clients:detail', kwargs={'pk': self.kwargs['pk']})
