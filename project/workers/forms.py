from django import forms
from .models import Employee

import core.forms

class EmployeeForm(
    core.forms.BootstrapClassFormMixin,
    core.forms.BootstrapPlaceholderFormMixin,
    forms.ModelForm
):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[
            Employee.birthday.field.name
        ].widget = forms.fields.TextInput({'type': 'date',})
        for field in self.fields.values():
            field.required = True

    class Meta:
        model = Employee
        exclude = ['zodiac_sign', 'age', 'significator', 'court_card']
