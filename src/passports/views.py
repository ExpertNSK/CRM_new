import datetime as dt
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Passport
from .forms import PassportForm
from loaders.models import Loader


def create_passport(request, pk):
    form = PassportForm(request.POST or None,
                        request.FILES or None)
    context = {
        'form': form,
        'pk': pk,
    }
    if request.method == 'POST':
        if form.is_valid():
            passport = form.save(commit=False)
            passport.save()
            Loader.objects.filter(pk=pk).update(
                passport = passport
            )
            return redirect('loaders:detail', pk=pk)
        return render(request, 'passports/create.html', context)
    return render(request, 'passports/create.html', context)

@csrf_exempt
def ajax_edit(request):
    if request.method == 'POST':
        passport = get_object_or_404(Passport, pk=request.POST['pid'])
        request.POST._mutable = True
        request.POST['date_of_issue'] = dt.datetime.strptime(request.POST['date_of_issue'], '%d-%m-%Y')
        request.POST['birthday'] = dt.datetime.strptime(request.POST['birthday'], '%d-%m-%Y')
        form = PassportForm(request.POST or None, request.FILES or None, instance=passport)
        if form.is_valid():
            form.save()
            passport = {
                'serial_number': passport.serial_number,
                'issued_by': passport.issued_by,
                'division_code': passport.division_code,
                'date_of_issue': dt.datetime.strftime(passport.date_of_issue, '%d %m %Y'),
                'last_name': passport.last_name,
                'first_name': passport.first_name,
                'middle_name': passport.middle_name,
                'birthday': dt.datetime.strftime(passport.birthday, '%d %m %Y'),
                'place_of_birth': passport.place_of_birth,
                'photo_main_page': str(passport.photo_main_page),
                'photo_registration': str(passport.photo_registration),
            }
            print(passport)
            return JsonResponse({'status': 'OK', 'passport_data': passport})
        return JsonResponse({'status': 'Unable to save'})
    return JsonResponse({'status': f'405 - Method {request.method} is not allowed.'})
