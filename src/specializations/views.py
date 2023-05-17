from typing import Any, Dict
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt

from .models import Specialization
from .forms import SpecializationForm


class ListSpecView(ListView):
    queryset = Specialization.objects.all()
    template_name = 'specializations/list.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = SpecializationForm
        return context

@csrf_exempt
def create_specializations(request):
    if request.method == 'POST':
        form = SpecializationForm(request.POST)
        if form.is_valid():
            specialization = request.POST['specialization']
            pid = request.POST.get('id')
            if pid == '':
                s = Specialization(specialization=specialization)
            else:
                s = Specialization(id=pid, specialization=specialization)
            s.save()
            specializations = Specialization.objects.values()
            specializations_data = list(specializations)
            return JsonResponse({'status': 'OK', 'specializations': specializations_data})
        return JsonResponse({'status': 'Unable to save'})
    return JsonResponse({'status': f'405. Method {request.method} is not allowed.'})

@csrf_exempt
def delete_specializations(request):
    if request.method == 'POST':
        pid = request.POST['pid']
        if Specialization.objects.filter(pk=pid).exists():
            Specialization.objects.filter(pk=pid).delete()
            return JsonResponse({'status': 'OK'})
        return JsonResponse({'status': f'Object with pid = {pid} is not found'})
    return JsonResponse({'status': f'405. Method {request.method} is not allowed.'})

def edit_specializations(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        if Specialization.objects.filter(pk=pid).exists():
            specialization = Specialization.objects.filter(pk=pid).get()
            specialization_data = {'id': specialization.id, 'specialization': specialization.specialization}
            return JsonResponse({'status': 'OK', 'specialization': specialization_data})
        return JsonResponse({'status': f'Object with pid = {pid} is not found'})
    return JsonResponse({'status': f'405. Method {request.method} is not allowed.'})
