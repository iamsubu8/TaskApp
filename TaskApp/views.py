from django.shortcuts import redirect, render
from .models import *
from .forms import * 
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def index(request):
    return render(request,"index.html")

# This fuction used for login user
def login(request):
    if request.method == "POST":       
        user = authenticate(
            username = request.POST.get("username"),
            password = request.POST.get("password")
        )
        #authenticate is a django pre-built method for login
        if user is not None:
            if user.is_active == True:
                auth_login(request, user)
                return redirect("index")
    context = {
        'form':LoginForm(),
        'type':'login'
    }
    return render(request, 'login.html', context=context) #passing loginform to template

#This function is for user signup
def SignUp(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.set_password(request.POST.get('password'))
            user.save()
            return redirect("login")
        print(form.errors)
    context = {
        'form':LoginForm(),
        'type':'signup'
    }
    return render(request, 'login.html', context=context)

#This function is for task functionality
def TaskPage(request):
    if request.method == "POST":
        #try except keywords used for error handling 
        try:
            taskForm = TaskForm(request.POST)
            if taskForm.is_valid:
                taskForm.save()
            print("taskForm",taskForm.errors)
        except Exception as e:
            print("error1", e)
        try:
            form = TaskStatusForm(request.POST)
            if (form.is_valid):
                taskStatus = form.save(commit=False)
                taskStatus.UserID = request.user
                taskStatus.save()
                return redirect("taskTable")
            print("taskStatusForm",form.errors)
        except Exception as e:
            print("error2", e)
        
    context = {
        'form':TaskStatusForm(),
        'taskForm':TaskForm(),
        'taskDatas': TaskStatusTable.objects.all()
    }
    return render(request, 'task.html', context=context)

#This function is for  to get all the data from the task table 
def TaskTable(request):
    context = {
        'taskDatas': TaskStatusTable.objects.all()
    }
    return render(request, 'taskTable.html', context=context)

#this function is for logout the user
def logout(request):
    auth_logout(request)
    return redirect("index")