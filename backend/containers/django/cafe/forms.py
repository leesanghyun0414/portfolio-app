#
# from django.forms import ModelForm
#
#
# from .models import Category, Drink, Food
# from .models import Menu
#
#
# class MenuForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(MenuForm, self).__init__(*args, **kwargs)
#         self.fields["category"].queryset = Category.categories.leaf_categories()
#
#     class Meta:
#         model = Menu
#         fields = ["name", "category", "calorie", "price", "image"]
#
#     # content = forms.ChoiceField(label="Content", choices=(("Food", "Food"), ("Drink", "Drink")))
#
#
# # class DrinkForm(ModelForm):
# #     class Meta:
# #         model = Drink
# #         fields = ["has_hot", "has_cold"]
# #         labels = {
# #             "has_hot": "Hot",
# #             "has_cold": "Cold"
# #         }
