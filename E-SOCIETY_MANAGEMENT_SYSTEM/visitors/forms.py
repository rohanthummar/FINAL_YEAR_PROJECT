from django import forms
from .models import Visitor


class VisitorForm(forms.ModelForm):

    class Meta:
        model = Visitor
        fields = ['visitor_name', 'phone', 'flat_number', 'purpose']