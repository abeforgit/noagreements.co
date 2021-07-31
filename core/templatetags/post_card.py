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
    pp_inc_url = reverse("inc_post_position", args=[post_position.id])
    pp_dec_url = reverse("dec_post_position", args=[post_position.id])
    result["pp_inc_url"] = '"' + pp_inc_url + '"'
    result["pp_dec_url"] = '"' + pp_dec_url + '"'
    result["has_pos"] = True
    result["pos"] = post_position.position
    result["editing"] = context["editing"]
    return result
