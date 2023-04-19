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
