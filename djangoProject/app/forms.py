from django import forms
from .models import ChaiVarity

class ChaiForm(forms.Form):
    chai_variety = forms.ModelChoiceField(queryset=ChaiVarity.objects.all(), empty_label=None)
    