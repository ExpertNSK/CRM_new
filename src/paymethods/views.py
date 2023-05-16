from django.shortcuts import redirect, render
from django.views.generic import ListView

from loaders.models import Loader
from .forms import PayMethodForm
from .models import PayMethod


class ListPayMethod(ListView):
    queryset = PayMethod.objects.all()
    template_name = 'paymethods/list.html'


def create_paymethod(request, pk):
    form = PayMethodForm(request.POST or None)
    context = {
        'form': form,
        'pk': pk
    }
    if request.method == 'POST':
        if form.is_valid():
            paymethod = form.save(commit=False)
            paymethod.save()
            Loader.objects.filter(pk=pk).update(
                paymethod=paymethod
            )
            return redirect('loaders:detail', pk=pk)
        return render(request, 'paymethods/create.html', context)
    return render(request, 'paymethods/create.html', context)

def create_payment_type(request):
    pass
