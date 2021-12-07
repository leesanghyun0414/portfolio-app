import logging
import logging.config
import sys

from django.forms.models import ModelForm

from cafe.models import Drink

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


class DrinkForm(ModelForm):
    class Meta:
        model = Drink
        exclude = ["menu_type"]

    def has_changed(self, *args, **kwargs) -> bool:
        """
        Check Drink form fields changed

        Parameters
        ----------
        args
        kwargs

        Returns
        -------

        """
        if self.instance.pk is None:
            return True
        return super(DrinkForm, self).has_changed()

    def clean(self) -> dict:
        """
        Check Drink temperature checked both or one.

        Returns
        -------
        self.cleaned_data : dict

        """
        logging.info(self.cleaned_data["has_cold"])
        if not (self.cleaned_data["has_hot"] or self.cleaned_data["has_cold"]):
            self.add_error(None, "Cold,Hotの両方又は片方にチェックを入れてください")

        return self.cleaned_data
