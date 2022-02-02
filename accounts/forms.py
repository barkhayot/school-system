from django import forms
from django.forms import ModelForm
from .models import Account

class StudentRegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    account_id = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Account ID'
    }))



    class Meta:
        model = Account
        fields = ['account_id', 'first_name', 'last_name', 'phone_number', 'email', 'password']


    def clean(self):
        cleaned_data = super(StudentRegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
            'Passwords do not match!'
        )


    def __init__(self, *args, **kwargs):
        super(StudentRegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder']='Enter Last Name'
        self.fields['email'].widget.attrs['placeholder']='Enter Email Address'
        self.fields['phone_number'].widget.attrs['placeholder']='Enter Phone Number'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'


class ProfessorRegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    account_id = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Confirm Password'
    }))


    class Meta:
        model = Account
        fields = ['account_id', 'first_name', 'last_name', 'phone_number', 'email', 'password']

    def clean(self):
        cleaned_data = super(ProfessorRegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
            'Passwords do not match!'
        )

    def __init__(self, *args, **kwargs):
        super(ProfessorRegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder']='Enter Last Name'
        self.fields['email'].widget.attrs['placeholder']='Enter Email Address'
        self.fields['phone_number'].widget.attrs['placeholder']='Enter Phone Number'
        self.fields['account_id'].widget.attrs['placeholder']='Enter Account ID'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
