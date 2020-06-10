from django import forms
from .models import Donate

class DonateBook(forms.ModelForm):
    class Meta:
        model = Donate
        fields = ('title','image','author','bookType','desc')
