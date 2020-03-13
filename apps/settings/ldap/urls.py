""" LDAP URL """
from .views import *
from django.urls import path


urlpatterns = [
    path('', LdapSettingsView.as_view(), name='ldap_config_url'),
    path('test_connect', LDAPTestConnect.as_view(), name='ldap_test_connect_url'),
    path('sync_user', sync_ldap_user, name='ldap_setting_sync_user_url'),
]