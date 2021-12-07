import logging
import logging.config
import sys

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .forms import SizeForm
from .forms.drink_form import DrinkForm
from .forms.food_form import FoodForm
from .forms.menu_form import MenuForm
from .forms.topping_form import ToppingForm
from .models import Size
from .models import Topping
from .models.category import Category
from .models.drink import Drink
from .models.food import Food
from .models.menu import Menu
from .types import MenuType

LOGGING = {
    "version": 1,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
        }
    },
    "root": {"handlers": ["console"], "level": "INFO"},
}

logging.config.dictConfig(LOGGING)


class DrinkInline(admin.TabularInline):
    model = Drink
    form = DrinkForm
    fk_name = "menu"

    fields = ["has_cold", "has_hot", "size"]
    extra = 0
    min_num = 0


class FoodInline(admin.TabularInline):
    model = Food

    fk_name = "menu"
    form = FoodForm
    extra = 0
    min_num = 0


class MyAdmin(TreeAdmin):
    list_display = [
        "name",
        "path",
        "depth",
    ]

    form = movenodeform_factory(Category)


class MenuAdmin(admin.ModelAdmin):
    form = MenuForm
    list_display = ["name", "image_tag"]
    inlines = [DrinkInline, FoodInline]

    def save_model(self, request, obj, form, change):

        category: Category = Category.categories.get(pk=request.POST.get("category"))
        logging.info(category.get_root())
        root_node: str = category.get_root().name
        logging.info(f"obj : {obj}")
        logging.info(f"Data : {self}")
        logging.info(f"request : {request.POST}")

        if root_node == MenuType.DRINK.label:
            obj.menu_type = Drink._meta.get_field("menu_type").get_default()
        elif root_node == MenuType.FOOD.label:
            obj.menu_type = Food._meta.get_field("menu_type").get_default()

        super().save_model(request, obj, form, change)


class DrinkAdmin(admin.ModelAdmin):
    model = Drink
    form = DrinkForm


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    model = Size
    form = SizeForm
    list_display = ["description", "constant_addition"]


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    model = Topping
    form = ToppingForm



admin.site.register(Category, MyAdmin)
admin.site.register(Menu, MenuAdmin)
