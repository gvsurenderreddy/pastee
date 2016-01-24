from django import template

register = template.Library()


@register.filter(name='addclass')
def addclass(val, args):
    return val.as_widget(attrs={'class': args})
