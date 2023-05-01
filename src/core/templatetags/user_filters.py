import datetime as dt
from django import template


register = template.Library()

@register.filter
def loader_filter(worktime, profile):
    return worktime.filter(loader=profile.id)

@register.filter
def start_day_id(field, id_value):
    return field.as_widget(attrs={'id': 'start' + id_value})

@register.filter
def end_day_id(field, id_value):
    return field.as_widget(attrs={'id': 'end' + id_value})

@register.filter
def get_day(workday, date: str):
    workday = workday.filter(day=dt.datetime.strptime(date.split()[0], '%d/%m/%Y'))
    if workday.exists():
        return f'{str(workday[0].start_time)[:5]} - {str(workday[0].end_time)[:5]}'
    return None
