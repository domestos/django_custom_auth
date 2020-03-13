from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.accounts.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('image','email','first_name','last_name','department')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     if email :
    #         if User.objects.filter(email=email):
    #             raise forms.ValidationError('this email already exist')
    #     return email