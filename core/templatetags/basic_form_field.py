from django import template
from django.forms import Field

register = template.Library()


@register.inclusion_tag("core/components/basic_form_field.html")
def basic_form_field(field: Field, id: str):
    return {"field": field, "id": id}
