from django import template
from django.urls import reverse

register = template.Library()


@register.inclusion_tag("core/components/sidebar_item.html")
def sidebar_item(label, url, slashes, *args):
    if args:
        revurl = reverse(url, args=args)
    else:
        revurl = reverse(url)
    return {"label": label, "url": revurl, "slashes": range(slashes)}
