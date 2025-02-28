from django.forms import ModelForm
from django import forms
from .models import Triangle

class TriangleForm(ModelForm):
    first_side = forms.DecimalField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 
        'placeholder': 'Введите первую сторону', 
        'min': '0.1', 'step': '0.1'}))
    second_side = forms.DecimalField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 
        'placeholder': 'Введите вторую сторону', 
        'min': '0.1', 'step': '0.1'}))
    third_side = forms.DecimalField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 
        'placeholder': 'Введите третью сторону', 
        'min': '0.1', 'step': '0.1'}))

    class Meta:
        model = Triangle
        fields = ['first_side', 'second_side', 'third_side']

triangle_form = TriangleForm()