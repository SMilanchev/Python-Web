from django import template

register = template.Library()


@register.filter()
def split_filter_func(value):
    return ','.join(list(value))

