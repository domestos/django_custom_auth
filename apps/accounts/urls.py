""" ACCOUNTS URL """

from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views import View
from .views import AccountsView, ProfileView, UserTable

from django.contrib.auth import views as auth_views
from django.conf.urls import url

from .views import *

urlpatterns = [
    path('', AccountsView.as_view(), name='accounts_url'),

    url(r'^signup/$', signup, name='signup_url'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout_url'),
    path('users', UserTable.as_view(), name='users_url'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile_url'),
    path('group/list', GroupList.as_view(), name='group_url'),
    path('group/create/', GroupCreate.as_view(), name='group_create_url'),
    path('group/<int:pk>/change/', GroupUpdate.as_view(), name='group_change_url'),
    path('group/<int:pk>/delete/', GroupDelete.as_view(), name='group_delete_url'),
    # path('profile/change_password', change_password, name='change_password_url'),
    # url(r'^select2/', include('django_select2.urls')),


    
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/registration/login.html'), name='login_url'),


    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/registration/password_reset.html',
            email_template_name='accounts/registration/password_reset_email.html',
            subject_template_name='accounts/registration/password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/registration/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/registration/password_reset_complete.html'),
        name='password_reset_complete'),

    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='accounts/registration/password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/registration/password_change_done.html'),
        name='password_change_done'),

]
