from django.forms import ModelForm

from cafe.models import Size


class SizeForm(ModelForm):
    class Meta:
        model = Size
        fields = ["description"]
