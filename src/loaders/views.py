from typing import Any, Dict
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from statuses.forms import StatusForm
from specializations.forms import SpecializationForm
from passports.forms import PassportForm
from loaders.models import Loader
from loaders.forms import CreateLoaderForm
from shedule.utils import create_call_result


class ListLoaderView(LoginRequiredMixin, ListView):
    queryset = Loader.objects.filter(is_active=True)
    template_name = 'loaders/list.html'


class CreateLoaderView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Loader
    form_class = CreateLoaderForm
    template_name = 'loaders/create.html'
    success_message = 'Профиль успешно добавлен'

    def get_success_url(self):
        create_call_result(self.object.id)
        return reverse_lazy('loaders:detail', args=(self.object.id,))
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['specs_form'] = SpecializationForm
        context['status_form'] = StatusForm
        return context


class DetailLoaderView(LoginRequiredMixin, DetailView):
    model = Loader
    template_name = 'loaders/detail.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = CreateLoaderForm(instance=self.get_object())
        context['passport_form'] = PassportForm(instance=self.get_object().passport)
        return context


class UpdateLoaderView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Loader
    form_class = CreateLoaderForm
    success_message = 'Профиль успешно сохранен!'

    def get_success_url(self) -> str:
        return reverse_lazy('loaders:detail', kwargs={'pk': self.object.id})
