from blog.models import Post
from core.templatetags import register


@register.inclusion_tag("core/post_card.html")
def post_card(post: Post):
    return {'post': post}
