from django import template
from django.urls import reverse

register = template.Library()


@register.inclusion_tag("core/components/link_button.html")
def link_button(label: str, type: str, url: str, *args):
    if args:
        revurl = reverse(url, args=args)
    else:
        revurl = reverse(url)
    return {"to": revurl, "label": label, "type": type}