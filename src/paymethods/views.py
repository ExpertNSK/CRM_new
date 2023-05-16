from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt

from loaders.models import Loader
from .forms import PayMethodForm, PaymentTypeForm
from .models import PayMethod, PaymentType


class ListPayMethod(ListView):
    queryset = PayMethod.objects.all()
    template_name = 'paymethods/list.html'


def create_paymethod(request, pk):
    form = PayMethodForm(request.POST or None)
    payment_type_form = PaymentTypeForm
    context = {
        'form': form,
        'payment_type_form': payment_type_form,
        'pk': pk
    }
    if request.method == 'POST':
        if form.is_valid():
            paymethod = form.save(commit=False)
            paymethod.save()
            Loader.objects.filter(pk=pk).update(
                pay_method=paymethod
            )
            return redirect('loaders:detail', pk=pk)
        return render(request, 'paymethods/create.html', context)
    return render(request, 'paymethods/create.html', context)

@csrf_exempt
def create_payment_type(request):
    if request.method == 'POST':
        form = PaymentTypeForm(request.POST)
        if form.is_valid():
            form.save()
            payment_types = PaymentType.objects.values()
            payment_type_data = list(payment_types)
            return JsonResponse({'status': 'OK', 'payment_types': payment_type_data})
        return JsonResponse({'status': 'Unable to save'})
    return JsonResponse({'status': f'405. Method {request.method} is not allowed.'})
