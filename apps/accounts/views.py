from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import PasswordChangeForm
from .forms import SignUpForm, ProfileForm
from .models import User
from django.contrib import messages
# Create your views here.


class AccountsView(View):
    def get(self, request):
        return render(request, 'accounts/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('accounts_url')
    else:
        form = SignUpForm()
    return render(request, 'accounts/registration/signup.html', {'form': form})

class ProfileView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if user != request.user:
            return redirect('login_url')
        form = ProfileForm(instance=user)
        form_pass = PasswordChangeForm(user=request.user)
        context = {'user': user, 'form': form,
                   'form_pass': form_pass, 'profile_active': 'active'}
        return render(request, 'accounts/profile.html', context)

    def post(self, request, pk):
        action = request.POST.get('action')
        user = get_object_or_404(User, pk=pk)
        form = ProfileForm(instance=user)
        form_pass = PasswordChangeForm(user=request.user)
        # Save profile
        if action == 'edit_profile':
            form = ProfileForm(request.POST or None,
                               request.FILES or None, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Updated successfully',
                                 extra_tags='alert-success')
                return redirect('profile_url', pk)
            else:
                context = {'form': form, 'form_pass': form_pass,
                     'edit_active': 'active'}
                return render(request, 'accounts/profile.html', context)
        # Save password
        if action == 'change_password':
            form_pass = PasswordChangeForm(
                data=request.POST, user=request.user)
            if form_pass.is_valid():
                form_pass.save()
                messages.success(
                    request, 'Password was changed seccussful. Pelease enter with new password.', extra_tags='alert-success')
                return redirect('login_url')
            else:
                messages.error(request,  "Error", extra_tags='alert-danger')
                context =  {'form': form, 'form_pass': form_pass, 'ch_pass_active': 'active'}
                return render(request, 'accounts/profile.html', context)

# def change_password(request):
#     if request.method == "POST":
#         # user = get_object_or_404(User, pk=pk )
#         form_pass = PasswordChangeForm(data=request.POST, user=request.user)
#         print(request.user)
#         if form_pass.is_valid():
#             form_pass.save()
#             return redirect('account_url')
#         else:
#             form_pass = PasswordChangeForm(request.POST)
#             # user = get_object_or_404(User, pk=pk )
#             # form = ProfileForm(instance=user)
#             return redirect('accounts_url')
