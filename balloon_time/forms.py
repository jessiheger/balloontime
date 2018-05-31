from django import forms
from .models import Party, Clown

class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ('title', 'description', 'location')

class ClownForm(forms.ModelForm):
    class Meta:
        model = Clown
        fields = ('name', 'description')

