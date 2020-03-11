from django.shortcuts import render, redirect
from  django.views import View
from django.contrib.auth import login 
from .forms import SignUpForm
# Create your views here.

class AccountsView(View):
    def get(self, request):
        return render(request, 'accounts/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts_url')
    else:
        form = SignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})