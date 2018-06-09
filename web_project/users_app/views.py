from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from users_app.forms import User_basic_form, User_profile_form

# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('search:page_search'))

def page_register(request):
    error_msg = None
    if request.method == 'POST':
        user_basic_info = User_basic_form(data=request.POST)
        user_profile_info = User_profile_form(data=request.POST)
        print("Status: POST request received")

        if 'register-button' in request.POST:
            if user_basic_info.is_valid() and user_profile_info.is_valid():
                print("Status: form entry is valid")

                user_basic_entry = user_basic_info.save()
                # Set hashed password for security
                user_basic_entry.set_password(user_basic_entry.password)
                user_basic_entry.save()

                user_profile_entry = user_profile_info.save(commit=False)
                # Links OneToOneField between user_profile_entry and user_basic_entry
                user_profile_entry.user_profile = user_basic_entry
                user_profile_entry.save()

                # Show thank you page
                return HttpResponseRedirect('login/thanks')
            else:
                # error_msg = user_basic_info.errors + ' ' + user_profile_info.errors
                print("Status: form entry is invalid", user_basic_info.errors, user_profile_info.errors)
        else:
            print("Form button submission error!")
    else:
        user_basic_info = User_basic_form()
        user_profile_info = User_profile_form()

    # Set Django template tag dictionary
    user_profile_tagdict = {
        'user_basic_form_key' : user_basic_info,
        'user_profile_form_key' : user_profile_info,
        'error_key' : error_msg
    }

    return render(request, 'users_app/page_register.html', context=user_profile_tagdict)

def page_login(request):
    error_msg = None
    if request.method == 'POST':
        user_basic_info = User_basic_form(data=request.POST)
        print("Status: POST request received")

        if 'login-button' in request.POST:
            print("Status: form entry is valid")
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('search:page_search'))
                else:
                    print("User account is not found.")
            else:
                print("Login authentication failed!")
                error_msg = 'Oops, the entered username and password combination appears to be invalid.'

        elif 'new-user-button' in request.POST:
            # Show register page
            return HttpResponseRedirect(reverse('users:page_register'))
        else:
            print("Form button submission error!")
    else:
        user_basic_info = User_basic_form()

    # Set Django template tag dictionary
    user_basic_tagdict = {
        'user_basic_form_key' : user_basic_info,
        'error_key' : error_msg
    }
        
    return render(request, 'users_app/page_login.html', context=user_basic_tagdict)

def page_tylogin(request):
    return render(request, 'users_app/page_tylogin.html')