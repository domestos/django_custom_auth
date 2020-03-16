from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.accounts.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.admin.widgets import FilteredSelectMultiple, AutocompleteSelectMultiple
from django_select2.forms import Select2MultipleWidget, Select2Widget
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('image','email','first_name','last_name','department','groups','user_permissions')

    
class GqoupForm(forms.ModelForm):  
    # permissions = forms.ModelMultipleChoiceField(queryset=Permission.objects.all(), widget=Select2MultipleWidget)
    class Meta:
        model = Group
        fields = ('name','permissions')
        widgets = {
            'permissions': Select2MultipleWidget,
            # "style":  '{background-color:#17a2b8}'
            'class': "text-info",
            # 'multiple ':"",
            # 'id':'inputInfo',
            # 'style':"border-color: #3c8dbc; box-shadow: none;"
            
        }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     if email :
    #         if User.objects.filter(email=email):
    #             raise forms.ValidationError('this email already exist')
    #     return email