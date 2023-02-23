import markdown
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

md = markdown.Markdown(extensions=['extra'])

@register.filter()
@stringfilter
def markdown(value):
    return md.convert(value)
