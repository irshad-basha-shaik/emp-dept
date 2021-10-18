from django import forms
from employee.models import School,Department


class EmployeeForms(forms.ModelForm):
    class Meta:
        model=School
        fields='__all__'

class EditForm(forms.ModelForm):
    id = forms.IntegerField(label='Edit object with following ID')

class saveForm(forms.ModelForm):
    id = forms.IntegerField(label='Edit object with following ID')