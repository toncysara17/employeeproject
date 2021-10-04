from django import forms
from .models import Employee
from django.forms import ModelForm

class SigninForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Enter Password'}))

class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['id']
        fields = ["name","email","address","mobile","gender"]
        widgets = {
                   "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Name"}),
                   "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Email"}),
                   "address": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter Address"}),
                   "mobile": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Mobile Number"}),
                   "gender": forms.TextInput(attrs={"class": "form-control"})
                   }