from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse
from basic_app.models.my_form import UserForm
from basic_app.models.my_form import UserInfoForm
from django.contrib.auth.hashers import make_password


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)
        if user_form.is_valid() and user_info_form.is_valid:
             user = user_form.save()
             user.set_password(user.password)
             user.save()

             myuser = user_info_form.save(commit = False)
             myuser.username = user
             myuser.save()
             registered =True
            
        else:
            print(user_form.errors,user_info_form.errors)
    else:
        user_form=UserForm()
        user_info_form = UserInfoForm()

    return render(request,'register.html',{'user_form':user_form,'user_info_form':user_info_form})