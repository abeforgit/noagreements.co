from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from core.models import TagPostPosition


def inc_post_position(request, postposition_id):
    if request.method != 'POST':
        return JsonResponse(status=404, data={})

    postposition = get_object_or_404(TagPostPosition, pk=postposition_id)
    nextpos = TagPostPosition.objects.filter(tag=postposition.tag,
                                             position__gt=postposition.position).order_by(
        "position").first()
    if nextpos is None:
        return JsonResponse(status=200, data={})
    nextpos.position = postposition.position
    nextpos.save()
    postposition.position += 1
    postposition.save()

    return JsonResponse(status=200, data={"new_nextpos": nextpos.position,
                                          "new_postpos": postposition.position})


def dec_post_position(request, postposition_id):
    pass
