from pathlib import Path

from django.conf import settings


def delete_previous_image(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        model = type(self)
        previous_obj = model.objects.filter(pk=self.pk)

        if previous_obj.exists():
            target_path = Path(settings.MEDIA_ROOT).joinpath(str(previous_obj[0].image))
            Path.unlink(target_path)

        return func(*args, **kwargs)

    return wrapper
