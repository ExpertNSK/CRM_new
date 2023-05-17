from typing import Any, Dict
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt

from .forms import StatusForm
from .models import Status


class ListStatusView(ListView):
    queryset = Status.objects.all()
    template_name = 'statuses/list.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = StatusForm
        return context

@csrf_exempt
def create_status(request):
    if request.method == 'POST':
        print(request.POST)
        form = StatusForm(request.POST)
        if form.is_valid():
            status = request.POST['status']
            pid = request.POST.get('id')
            if pid == '':
                s = Status(status=status)
            else:
                s = Status(id=pid, status=status)
            s.save()
            status_list = Status.objects.values()
            status_data = list(status_list)
            return JsonResponse({'status': 'OK', 'status_data': status_data})
        return JsonResponse({'status': 'Unable to save'})
    return JsonResponse({'status': f'405. Method {request.method} is not allowed.'})

@csrf_exempt
def delete_status(request):
    if request.method == 'POST':
        pid = request.POST['pid']
        if Status.objects.filter(pk=pid).exists():
            Status.objects.filter(pk=pid).delete()
            return JsonResponse({'status': 'OK'})
        return JsonResponse({'status': f'Object with pid = {pid} is not found'})
    return JsonResponse({'status': f'405. Method {request.method} is not allowed.'})

def edit_status(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        if Status.objects.filter(pk=pid).exists():
            status = Status.objects.filter(pk=pid).get()
            json = {'id': status.id, 'status': status.status}
            return JsonResponse({'status': 'OK', 'json': json})
        return JsonResponse({'status': f'Object with pid = {pid} is not found'})
    return JsonResponse({'status': f'405. Method {request.method} is not allowed.'})
