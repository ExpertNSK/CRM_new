import datetime as dt
from django.shortcuts import render
from shedule.forms import UpdateWorkDayForm

from shedule.models import CallResult, WorkShedule

from .utils import check_callstatus, get_dates, get_loaders, workdays_create


def shedule_view(request):
    dates, date_filter = get_dates(curr_week=True)
    loaders = get_loaders()
    workdays = WorkShedule.objects.filter(
        day__range=(
            dt.datetime.strptime(dates[0].split()[0], '%d/%m/%Y'),
            dt.datetime.strptime(dates[-1].split()[0], '%d/%m/%Y')
        )
    )
    context = {
        'dates': dates,
        'date_filter': date_filter,
        'loaders': loaders,
        'workdays': workdays,
    }
    return render(request, 'shedule/shedule.html', context)


def calling(request):
    form = UpdateWorkDayForm
    loaders = get_loaders()
    call_results = CallResult.objects.all()
    dates, _ = get_dates(curr_week=True)
    context = {
        'loaders': loaders,
        'call_results': call_results,
        'dates': dates,
        'form': form,
    }
    if request.method == 'POST':
        if not check_callstatus(request):
            pass
        else:
            workdays_create(request, dates)
    return render(request, 'shedule/calling.html', context)
