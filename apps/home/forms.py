from django import forms

from .models import HomeTestModel


class TestForm(forms.ModelForm):
    
    class Meta:
        model = HomeTestModel
        fields = ("title", "subtitle", "quantity")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Enter text here"
                }
            )
        }

    def clean_quantity(self):
        quantity = self.clean_quantity["quantity"]
        if quantity < 10:
            raise forms.ValidationError("Enter a number greater than 10")
        return quantity
