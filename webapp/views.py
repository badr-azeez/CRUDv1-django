from django.shortcuts import render , redirect
# Create your views here.
from django.urls import reverse
from .forms import CreateUserForm , LoginForm , CreateRecordForm , UpdateRecordForm

from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required 
from .models import Record
from django.contrib import messages

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    return render(request,'webapp/index.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Account Was Created!")
            return redirect('login')
        else:
            print('not valid')
        
    context = {'form':form}
    return render(request,'webapp/register.html',context=context)

def my_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return  redirect('dashboard')
    context = {"form":form}     
    return render(request,'webapp/my-login.html',context=context)

@login_required(login_url='login')
def my_logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    records = Record.objects.all()
    context = {'records':records}
    return render(request,'webapp/dashboard.html',context=context)

@login_required(login_url='login')
def CreateRecord(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Record Was Created!")
            return redirect('dashboard')
            
    context = {'form':form}
    return render(request,'webapp/create-record.html',context=context)

@login_required(login_url='login')
def UpdateRecord(request,pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Record Was Updated!")
            return redirect('dashboard')
    context= {"form":form}
    return render(request,'webapp/update-record.html',context=context)


@login_required(login_url='login')
def SingleRecord(request,pk):
    record = Record.objects.get(id=pk)
    if request.method == 'POST':
        record.delete()
        messages.success(request,"Your Record Was Deleted!")
        return redirect('dashboard')
    context= {'record':record}
    return render(request,'webapp/view-record.html',context=context)