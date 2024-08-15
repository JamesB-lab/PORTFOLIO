import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.contrib.staticfiles.storage import staticfiles_storage
import re

register = template.Library()

md = markdown.Markdown(extensions=['extra'])

pattern = r'src=\"/static/([^\"]+)\"'

def sign_func(match) -> str:
    captured_value = match.group(1)
    return f'src="{staticfiles_storage.url(captured_value)}"'

@register.filter()
@stringfilter
def markdown(value):
    text = md.convert(value)
    signed_text = re.sub(pattern, sign_func, text)
    return signed_text
