from django.forms import ModelForm
from django.forms import ImageField, FileInput
from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer']



class CustomerForm(ModelForm):
    img = ImageField(widget=FileInput)
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'slug']