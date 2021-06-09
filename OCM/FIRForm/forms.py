from django import forms
from django.utils import timezone
from .models import FIR

class FIR_Form(forms.ModelForm):
    class Meta:
        model = FIR
        fields = ["city","state","zip","PoliceStation","VicFN","VicLN","ComplaintType","Description","ComFN","ComLN","publish","Email"]
        
class  SearchForm(forms.Form):
    query = forms.CharField()       