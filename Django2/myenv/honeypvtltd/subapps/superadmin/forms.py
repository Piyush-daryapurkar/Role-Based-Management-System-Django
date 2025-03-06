from django import forms
from .models import Manager_data

state_choice=((
    "mp","madhyapradesh",
))
    
class ManagerForm(forms.ModelForm):
    class Meta:
        model=Manager_data
        fields=['name','email','password','birth_date','joining_date','emp_id']
    
class Manager_aditional_data(forms.Form):
    image=forms.ImageField()
    pancard=forms.CharField(max_length=10)
    aadharcard=forms.CharField(max_length=12)
    address=forms.CharField(max_length=150)
    state=forms.ChoiceField(choices=state_choice)
    
class Manager_login_form(forms.Form):
    email=forms.EmailField(label="Enter your Email")
    password=forms.CharField(label="Enter your password")
    
