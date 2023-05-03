from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .forms import CreateClientForm
from .models import Client


class ListClientView(LoginRequiredMixin, ListView):
    queryset = Client.objects.filter(is_active=True)
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


class DeleteClientView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clients:list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.__class__.objects.filter(pk=self.object.id).update(
            is_active=False
        )
        return HttpResponseRedirect(self.success_url)

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Контрагент успешно удален')
        return self.post(request, *args, **kwargs)
