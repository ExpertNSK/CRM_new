from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from users.models import CustomUser
from users.forms import CustomUserEditForm


class CustomUserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    queryset = CustomUser.objects.filter().exclude(role='Грузчик')
    template_name = 'staff/list.html'


class CustomUserDetailView(SuccessMessageMixin, LoginRequiredMixin, DetailView, UpdateView):
    model = CustomUser
    template_name = 'staff/detail.html'
    form_class = CustomUserEditForm
    success_message = 'Сотрудник успешно отредактирован'

    def get_success_url(self):
        return reverse_lazy('staff:detail', args=(self.object.id,))
