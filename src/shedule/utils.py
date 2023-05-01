import datetime as dt

from loaders.models import Loader
from .models import CallResult, WorkShedule
from .lists import CALL_RESULTS_NEGATIVE, WEEKDAYS_RUS


def get_dates(request=None, curr_week=False, next_week=False):
    today = dt.datetime.now()
    one_day = dt.timedelta(days=1)
    dates = []
    if curr_week:
        while today.weekday() != 0:
            today -= one_day
        start_day = today
        date_filter = False
    if next_week:
        while today.weekday() != 0:
            today += one_day
        start_day = today
        date_filter = False
    end_day = start_day + dt.timedelta(days=6)
    while start_day != (end_day + one_day):
        dates.append(
            f'{start_day.strftime("%d/%m/%Y")} '
            f'{WEEKDAYS_RUS[start_day.weekday()]}'
        )
        start_day += one_day
    return dates, date_filter
    
        
def get_loaders(request=None):
    return Loader.objects.filter(is_active=True)

def create_call_result(id):
    CallResult.objects.create(
        loader = Loader.objects.get(id=id),
        last_call_result = None,
        date_last_call = None,
        comment = None,
        day_get_last_status = None
    )

def workdays_create(request, dates):
    loader = request.POST.get('loader')
    start_times = request.POST.getlist('start_time')
    end_times = request.POST.getlist('end_time')
    shedule = {}
    for i in range(len(dates)):
        shedule[dates[i]] = {
            'start': start_times[i],
            'end': end_times[i]
        }
    for i in range(len(shedule)):
        day = dt.datetime.strptime(dates[i][:10], '%d/%m/%Y')
        if (
            not shedule[dates[i]]['start']
            or not shedule[dates[i]]['end']
        ):
            WorkShedule.objects.filter(
            loader=Loader.objects.get(id=loader),
            day=day,
            ).delete()
            continue
        WorkShedule.objects.update_or_create(
            loader=Loader.objects.get(id=loader),
            day=day,
            defaults={
               'start_time': shedule[dates[i]]['start'],
               'end_time': shedule[dates[i]]['end'], 
            }
        )


def check_callstatus(request):
    call_status = request.POST.get('call_status')
    loader = request.POST.get('loader')
    object = CallResult.objects.filter(
        loader=loader
    )
    return True