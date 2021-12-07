from django.forms import ModelForm

from cafe.models import Topping


class ToppingForm(ModelForm):
    class Meta:
        model = Topping
        fields = "__all__"
