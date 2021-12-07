from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class MenuType(TextChoices):
    DRINK = "DK", _("Drink")
    FOOD = "FD", _("Food")


class DrinkSizeType(TextChoices):
    XLARGE = "XL", _("XLarge")
    LARGE = "L", _("Large")
    SMALL = "S", _("Small")
    MEDIUM = "M", _("Medium")


OPTION_TYPE = [
    (
        "Topping",
        (
            "Size",
            (
                ("M", ""),
                ("L", "Large"),
                ("XL", "XLarge"),
            ),
        ),
    )
]
