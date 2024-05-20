from django import forms

# Reorder Form and View


class PositionForm(forms.Form):
    position = forms.CharField()