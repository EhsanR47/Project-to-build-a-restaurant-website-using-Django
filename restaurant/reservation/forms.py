from django import forms
from django.forms import fields
from .models import Reservation
# class ReservationForm(forms.Form):
#     name = forms.CharField(max_length=200,required=False)
#     email = forms.EmailField(max_length=200, required=False)
#     phone = forms.IntegerField(max_length=200, required=True)
#     . . .

#or
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"

