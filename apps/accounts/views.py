from django.shortcuts import render, redirect
from  django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

# Create your views here.

class AccountsView(View):
    def get(self, request):
        return render(request, 'accounts/index.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts_url')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})