from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Profile
from .form import Login_Form, Update_User_Form, UserCreationForms, Update_Profile_Form
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def doctors_List(request):
    doctor = User.objects.all()
    return render(request, 'user/doctors_List.html', {'doctors': doctor,})


def doctors_details(request, slug):
    doctor_detail = Profile.objects.get(slug=slug)
    return render(request, 'user/doctors_details.html', {'doctor_detail': doctor_detail,})


def user_login(request):
    if request.method == 'POST':
        form = Login_Form()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:doctors_List')
    else:
        form = Login_Form()
    return render(request, 'user/login.html', {'form':form})


@login_required()
def myprofile(request):
    return render(request, 'user/myprofile.html', {})


def signup(request):
    user_signup = UserCreationForms()
    if request.method == "POST":
        user_signup = UserCreationForms(request.POST)
        if user_signup.is_valid():
            user_signup.save()
            username = user_signup.cleaned_data.get('username')
            password = user_signup.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('accounts:doctors_List')
    else:
        user_signup = UserCreationForms()
    return render(request, 'user/signup.html', {'user_signup':user_signup})


def update_profile(request):
    user_form = Update_User_Form(instance=request.user)
    profile_form = Update_Profile_Form(instance=request.user.profile)
    if request.method == "POST":
        user_form = Update_User_Form(request.POST, instance=request.user)
        profile_form = Update_Profile_Form(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('accounts:doctors_List')

    return render(request, 'user/update_profile.html', {'user_form':user_form, 'profile_form':profile_form, })