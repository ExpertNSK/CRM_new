from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView
from orders.forms import CreateOrderForm

from orders.models import Order


class OrdersListView(LoginRequiredMixin, ListView):
    queryset = Order.objects.all()
    template_name = 'orders/list.html'


class OrderDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView, UpdateView):
    model = Order
    form_class = CreateOrderForm
    template_name = 'orders/detail.html'
    success_message = 'Заявка успешно сохранена'
