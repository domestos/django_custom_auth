from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import PasswordChangeForm
from .forms import SignUpForm, ProfileForm, GqoupForm
from .models import User
from django.contrib import messages
from .decorators import unaunthenticated_user
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from .profile_permissions import ProfilePermissionsMixin
from django.urls import reverse_lazy

from django.views.generic import ListView, FormView
from django.views.generic.edit import UpdateView, CreateView , DeleteView
from django.contrib.auth.models import Group, Permission

# @login_required
class AccountsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'accounts/index.html')

@unaunthenticated_user
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

class ProfileView(LoginRequiredMixin, PermissionRequiredMixin, View):

    # login_url = None  
    permission_required=  ('accounts.view_user', 'accounts.change_user') 
    permission_denied_message = 'accounts.view_user'
    # raise_exception = False
    # redirect_field_name = REDIRECT_FIELD_NAME


    # @method_decorator(permission_required('accounts.view_user', 'accounts.change_user'))
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        # if user != request.user:
        #     return redirect('login_url')
        form = ProfileForm(instance=user)
        form_pass = PasswordChangeForm(user=request.user)
        context = {'user': user, 'form': form,
                   'form_pass': form_pass, 'profile_active': 'active'}
        return render(request, 'accounts/profile.html', context)
    
    # @method_decorator(permission_required('accounts.change_user', login_url="accounts_url", raise_exception=True))
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



class GroupListView(PermissionRequiredMixin, ListView,FormView):
    permission_required=  ('auth.view_group') 
    template_name = 'accounts/group_view.html'
    model = Group
    form_class = GqoupForm

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context

class GroupUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required=  ( 'auth.change_group') 
    model = Group
    template_name = 'accounts/group_update.html'
    form_class = GqoupForm
    success_url = reverse_lazy('group_url')


class GroupCreateView(PermissionRequiredMixin , CreateView,FormView):
    permission_required=  ( 'auth.add_group','auth.view_group') 
    model = Group
    template_name = 'accounts/group_create.html'
    # fields = ['name','permissions']
    success_url = reverse_lazy('group_url')
    form_class = GqoupForm



class GroupDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required=  ('auth.delete_group','auth.view_group') 
    model = Group
    template_name = 'accounts/group_delete.html'
    success_url = reverse_lazy('group_url')