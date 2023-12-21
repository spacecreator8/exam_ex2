from django.contrib.auth import get_user_model
from django import forms

from app.models import ProductAndService


class AddOfferForm(forms.ModelForm):
    class Meta:
        model = ProductAndService
        fields = ['offer', 'name', 'description', 'email', 'phone', 'photo']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
            'email': forms.EmailInput(attrs={'type': 'email'}),
            'photo': forms.ClearableFileInput(),
        }
