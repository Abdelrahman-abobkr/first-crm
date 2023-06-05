from django.shortcuts import redirect
from django.http import HttpResponse



def User_Authenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func



def allowed_users(allowed_rolles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_rolles:
                return view_func(request, *args, **kwargs)
            
            else:
                return HttpResponse('<h1>Your Are Not Autharized To View This Page</h1><a href="/">Back To Home Page</a>')
        return wrapper_func
    return decorator



def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if 'customer' in group:
            return redirect('profile')

        if 'admin' in group:
            return view_func(request, *args, **kwargs)
    return wrapper_func