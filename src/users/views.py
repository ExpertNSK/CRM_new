from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from users.forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserEditForm
from users.models import CustomUser


def login_view(request):
    form = CustomAuthenticationForm(request.POST or None)
    if form.is_valid():
        phone = form.cleaned_data.get('phone')
        password = form.cleaned_data.get('password')
        user = authenticate(phone=phone, password=password)
        login(request, user)
        return redirect('staff:list')
    return render(request, 'users/login.html', {'form': form})


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('staff:list')
    template_name = 'users/signup.html'


class EditProfileView(SuccessMessageMixin, LoginRequiredMixin, DetailView, UpdateView):
    model = CustomUser
    form_class = CustomUserEditForm
    template_name = 'users/profile.html'
    success_message = 'Изменения сохранены'

    def get_success_url(self):
        return reverse_lazy('users:edit', args=(self.object.id,))
