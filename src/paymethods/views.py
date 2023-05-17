from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt

from loaders.models import Loader
from .forms import PayMethodForm, PaymentTypeForm
from .models import PaymentType


class ListPayMethod(ListView):
    queryset = PaymentType.objects.all()
    template_name = 'paymethods/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PaymentTypeForm()
        return context


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
        print(request.POST)
        form = PaymentTypeForm(request.POST)
        if form.is_valid():
            payment_type = request.POST['payment_type']
            pid = request.POST.get('id')
            if pid == '':
                pmtype = PaymentType(payment_type=payment_type)
            else:
                pmtype = PaymentType(id=pid, payment_type=payment_type)
            pmtype.save()
            payment_types = PaymentType.objects.values()
            payment_type_data = list(payment_types)
            return JsonResponse({'status': 'OK', 'payment_types': payment_type_data})
        return JsonResponse({'status': 'Unable to save'})
    return JsonResponse({'status': f'405. Method {request.method} is not allowed.'})

@csrf_exempt
def delete_payment_type(request):
    if request.method == 'POST':
        pid = request.POST['pid']
        if PaymentType.objects.filter(pk=pid).exists():
            PaymentType.objects.filter(pk=pid).delete()
            return JsonResponse({'status': 'OK'})
        return JsonResponse({'status': f'Object with pid = {pid} is not found'})
    return JsonResponse({'status': f'405. Method {request.method} is not allowed.'})

def edit_payment_type(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        if PaymentType.objects.filter(pk=pid).exists():
            payment_type = PaymentType.objects.filter(pk=pid).get()
            payment_type_data = {'id': payment_type.id, 'payment_type': payment_type.payment_type}
            return JsonResponse({'status': 'OK', 'payment_type': payment_type_data})
        return JsonResponse({'status': f'Object with pid = {pid} is not found'})
    return JsonResponse({'status': f'405. Method {request.method} is not allowed.'})
