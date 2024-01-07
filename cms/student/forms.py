from django import forms
from . models import Student

class StudentCreation(forms.Form):
    student_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Student Name ....'
    }))

    student_email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder' :'Student Email ....'
    }))

    student_contact = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Student Contact .....'
    }))
    
    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)

        super(StudentCreation, self).__init__(*args, **kwargs)

        if instance:
            self.fields['student_name'].initial = instance.s_name
            self.fields['student_email'].initial = instance.s_email
            self.fields['student_contact'].initial = instance.s_contact