from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import resolve
def unaunthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
           return redirect('accounts_url')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            print('start working allowed_users decorator')
            group = None
            current_url = resolve(request.path_info).url_name
            print(current_url)
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:         
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request,  "You don't have enough permissions" , extra_tags='alert-danger' )
                return redirect('accounts_url')    
        return wrapper_func
    return decorator
    