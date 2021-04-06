import bleach

_ALLOWED_TAGS = [
    'a', 'abbr', 'acronym', 'b', 'blockquote',
    'code', 'em', 'i', 'li', 'ol', 'strong', 'ul',
    'iframe', 'p', 'img', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'
]
_ALLOWED_ATTRS = {
    'a': ['href', 'title'], 'abbr': ['title'],
    'acronym': ['title'],
    'iframe': ['style', 'src', 'seamless', 'allow', 'allowfullscreen', 'height',
               'width', 'name', 'srcdoc', 'class', 'id', 'title', 'frameborder'],
    'img': ['alt', 'src']
}
_ALLOWED_STYLES = [
    'border', 'width', 'height'
]


def sanitize(content: str):
    return bleach.clean(content, tags=_ALLOWED_TAGS, attributes=_ALLOWED_ATTRS,
                        styles=_ALLOWED_STYLES)
