from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from core.models import TagPostPosition


def inc_post_position(request, postposition_id):
    if request.method != 'POST':
        return JsonResponse(status=404, data={})

    current_position = get_object_or_404(TagPostPosition, pk=postposition_id)
    next_position = TagPostPosition.objects.order_by(
        "position").filter(tag=current_position.tag,
                           position__gt=current_position.position).first()
    if next_position is None:
        return JsonResponse(status=200, data={})
    next_position.position = current_position.position
    current_position.position += 1
    next_position.save()
    current_position.save()

    return JsonResponse(status=200, data={
        "new_position_of_current": current_position.position,
        "new_position_of_next": next_position.position})


def dec_post_position(request, postposition_id):
    if request.method != 'POST':
        return JsonResponse(status=404, data={})

    current_position = get_object_or_404(TagPostPosition, pk=postposition_id)
    previous_position = TagPostPosition.objects.order_by(
        "position").filter(tag=current_position.tag,
                           position__lt=current_position.position).last()
    if previous_position is None:
        return JsonResponse(status=200, data={})
    previous_position.position = current_position.position
    current_position.position -= 1
    previous_position.save()
    current_position.save()

    return JsonResponse(status=200, data={
        "new_position_of_current": current_position.position,
        "new_position_of_previous": previous_position.position})
    pass
