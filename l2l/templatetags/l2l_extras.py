from django import template
import datetime
from time import strptime

register = template.Library()

@register.filter
def new_date_format(oldFormat):
    if(type(oldFormat) is str):
        return datetime.datetime.strptime(oldFormat, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
    elif(type(oldFormat) is datetime.datetime ):
        return oldFormat.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return ('Date is not a supported format.')