from django.forms.fields import BooleanField
from django.forms.models import ModelForm

from ..models.food import Food


class FoodForm(ModelForm):
    confirm_field = BooleanField(
        required=True, label="Check", help_text="食事メニューを追加する場合はチェックを入れてください"
    )

    class Meta:
        model = Food
        exclude = ["menu_type"]
