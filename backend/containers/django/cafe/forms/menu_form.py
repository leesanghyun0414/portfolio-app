import logging
import logging.config
import sys

from django.forms import ModelForm
from django.forms import forms
from django.forms.fields import CharField
from django.forms.widgets import MultiWidget
from django.forms.widgets import TextInput

from ..models.category import Category
from ..models.menu import Menu

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


class MenuForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.categories.leaf_categories()

    class Meta:
        model = Menu
        fields = "__all__"
        exclude = ["menu_type"]

    def clean(self) -> dict:
        total_forms = self._get_total_forms()
        logging.info(f"cleaned_data:{self.cleaned_data}")
        logging.info(self.data)
        logging.info(total_forms)

        if total_forms == 0:
            msg = "Optionsを入力してください"
            logging.error(msg)
            self.add_error(None, msg)
        elif total_forms >= 2:
            msg = "Optionsが重複しています"
            self.add_error(None, msg)

        return self.cleaned_data

    def _get_total_forms(self) -> int:
        form_count = 0

        for k, v in self.data.items():
            if "TOTAL_FORMS" in k:
                form_count += int(v)
        return form_count
