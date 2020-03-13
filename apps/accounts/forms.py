from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.accounts.models import User

class SignUpForm(UserCreationForm):
    # email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class ProfileForm(forms.ModelForm):
    # email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('email','first_name','last_name','department')

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     if email :
    #         if User.objects.filter(email=email):
    #             raise forms.ValidationError('this email already exist')
    #     return email