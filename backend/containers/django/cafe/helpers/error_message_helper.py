from django.core.checks import Error
from django.db.models import Model


def menu_type_error(obj):
    return [
        Error(
            f"Not correctly menu type.",
            hint="menu type must be : D (drink) or F (food).",
            obj=obj,
            id="app.E001",
        )
    ]
