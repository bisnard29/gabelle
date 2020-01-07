from django import forms
from .models import Order
from django.views.generic.edit import FormView


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product', 'site', 'size', 'type')
