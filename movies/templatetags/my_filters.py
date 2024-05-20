from django import template

register = template.Library()

@register.filter(name='times') 
def times(number):
    return range(number)
    
@register.filter(name='minutes_format')
def format_duration(minutes):
    """
    Converts minutes into hours and minutes format.
    """
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}h {remaining_minutes}m"