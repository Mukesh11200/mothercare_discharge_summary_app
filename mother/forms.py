from django import forms
from.models import dischargepatient


class dischargeform(forms.ModelForm):
    class Meta:
        model = dischargepatient
        fields = '__all__'