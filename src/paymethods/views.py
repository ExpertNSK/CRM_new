from django.shortcuts import render
from django.views.generic import ListView

from .models import PayMethod, PaymentType


class ListPayMethod(ListView):
    queryset = PayMethod.objects.all()
    template_name = 'paymethods/list.html'
