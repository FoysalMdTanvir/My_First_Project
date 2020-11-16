from django import template


register = template.Library()

def my_filter(value, arg):
    return value + "This is a string from custom filter"+' ' + arg


register.filter('custom_filter', my_filter)
