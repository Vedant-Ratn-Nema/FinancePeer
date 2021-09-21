from django import forms
from django.contrib.auth.forms import UserCreationForm
from Account.models import UserAccount
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
    email= forms.EmailField(max_length=60,help_text='Required add a valid email')
    workplace =forms.CharField(max_length=30,required=False)
    class Meta:
        model = UserAccount
        fields = ('email','first_name','last_name','gender','dob','about_me','collage','school','workplace','nationality')


class LoginForm(forms.ModelForm):
    password=forms.CharField(label='password',widget=forms.PasswordInput)

    class Meta:
        model=UserAccount
        fields = ('email','password')

    def clean(self):
        email=self.cleaned_data['email']
        password=self.cleaned_data['password']
        if not authenticate(email=email,password=password):
            raise forms.ValidationError("Invalid login")
