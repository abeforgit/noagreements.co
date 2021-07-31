from django import template
from django.urls import reverse

from core.models import TagPostPosition

register = template.Library()


@register.inclusion_tag("core/components/post_card.html", takes_context=True)
def post_card(context, post, tag):
    result = {"perms": context["perms"], "has_pos": False, "post": post}
    post_position = TagPostPosition.objects.filter(post=post, tag=tag).first()
    if post_position is None:
        return result
    pp_url = reverse("inc_post_position", args=[post_position.id])
    result["pp_url"] = '"' + pp_url + '"'
    result["has_pos"] = True
    result["pos"] = post_position.position
    return result
