from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse
from basic_app.models.my_form import UserForm
from django.contrib.auth.hashers import make_password


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
             user = user_form.save(commit=False)
             make_password(user.password)
             user.save()
             registered =True
            
        else:
            print(user_form.errors)
    else:
        user_form=UserForm()


    return render(request,'register.html',{'user_form':user_form})