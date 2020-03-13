from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import LdapSettingsForm
from .models import LdapSettings
from django.contrib import messages

from apps.settings.ldap.util.ldap import authenticate, test_connect, sync_users
# Create your views here.


class LdapSettingsView(View):
    def get(self, request):
        ldap_config = LdapSettings.objects.all().first()
        if(ldap_config is not None):
            ldap_config.LDAP_PASS = ldap_config.decrypt_pass(
                ldap_config.LDAP_PASS)
        forms = LdapSettingsForm(instance=ldap_config)
        return render(request, 'ldap/index.html', {'forms': forms})

    def post(self, request):
        ldap_config = LdapSettings.objects.all().first()
        bound_forms = LdapSettingsForm(request.POST, instance=ldap_config)
        if bound_forms.is_valid():
            bound_forms.save()
            return redirect('ldap_config_url')

        # if request.POST['test_connect_btn']:
        #     print("run test connect")
        #     return redirect('ldap_config_url')


class LDAPTestConnect(View):
    def get(self, request):
        print("=================================run test connect")
        connect_status = test_connect()
        if connect_status == True:
             print('=================================', connect_status)
             messages.success(request, connect_status, extra_tags='alert-success')
        else:
            messages.error(request,  "Failed connect. Please see the log. Valera, please, don't forget to write a log-system" , extra_tags='alert-danger' )
        return redirect('ldap_config_url')



def sync_ldap_user(request):
    if sync_users():
        messages.success(request, "Success", extra_tags='alert-success')
    else:
        messages.error(request,  "Failed connect. Please see the log. Valera, please, don't forget to write a log-system" , extra_tags='alert-danger' )
    return redirect('ldap_config_url')
