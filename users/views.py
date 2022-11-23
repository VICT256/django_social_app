from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from .forms import SignupForm, LoginForm, UpdateForm, ProfileForm
from .models import Profile, Contact



def register(request):
    if request.method == "POST":
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            signupform.save()
            messages.success(request, "Registration complete")
            return redirect("login")
        else:
            print(signupform.errors)
            print(signupform.non_field_errors)
            messages.error(request, "registration unsuccessful")
    else:
        signupform = SignupForm
    return render(request, 'users/register.html', { 'signupform': signupform })


def user_login(request):
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        if loginform.is_valid():           
            user = authenticate(request, username = loginform.cleaned_data.get('username'), password = loginform.cleaned_data.get('password')  )
            if user is not None:
                if user.is_active:
                    login(request, user)                  
                    messages.success(request, "login successfull")
                    return redirect('home')
            else:
                print(loginform.errors)
                print(loginform.non_field_errors)
                messages.error(request, "incorrect username or password")
        else:
            print(loginform.errors)
            print(loginform.non_field_errors)
            messages.error(request, "incorrect username or password")
    else:
        loginform = LoginForm()
    return render(request, 'users/login.html', { 'loginform': loginform })

@login_required
def profile(request, username):
    profile = User.objects.filter(username=username).first()
    return render(request, 'users/profile.html', {'profile': profile})

@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UpdateForm(data=request.POST, instance=request.user)
        profile_form = ProfileForm(data=request.POST, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile', request.user.username)
    else:
        user_form = UpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/profile-update.html', context)

    
@require_POST
@ajax_required
@login_required
def users_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try: 
            user = User.objects.get(id=user_id)
            if action == "follow":
                Contact.objects.create(user_follower=request.user.profile, user_followed=user.profile)
            else:
                Contact.objects.filter(user_follower=request.user.profile, user_followed=user.profile).delete()
            return JsonResponse({'status': 'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error'})
    return JsonResponse({'status': 'error'})
                
