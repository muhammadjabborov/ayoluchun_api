def update_view_count(model_class, obj, user, device_id):

    if user.is_authenticated:
        model_class.objects.update_or_create(
            course=obj,
            user=user,
        )
    elif device_id is not None:
        model_class.objects.update_or_create(
            course=obj,
            device_id=device_id
        )