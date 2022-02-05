
from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from .forms import ProfileForm, UserForm
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required





# register a new user function 
def register(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)   
        if user_form.is_valid():
            user = user_form #save user using default django authentification 
            user.save()
            return HttpResponseRedirect('/')        

        else:
            messages.success(request, user_form.errors)

    else:
        user_form=UserForm()

    content ={
        'form':user_form}
    return render(request, 'register.html', content)       
            
# authenticate a user             
def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("success")
    else:
        return render(request, 'login.html')  

# after succeed to login
def success(request):
    nui = UserProfile.objects.filter(user=request.user)
   
    return render(request, 'success.html', {"nui":nui})        

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# Create your views here.
# This function will help to valid data and save()
def create(request, *args, **kwargs):
    if request.method == "POST":
        form = ProfileForm(data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False) # We avoid commid here because we want to link to and existing user
            profile.user = request.user 
            profile.save()
            messages.success(request, 'Data was successfully save....thank')
            form = ProfileForm()
            object = UserProfile.objects.all()
            long = len(object)
            id = object[long-1]
            return render(request, 'index.html', {'form':form, 'object':id})

        else:
            form = ProfileForm(data=request.POST)
            messages.error(request, form.errors)
            
    else:
        form = ProfileForm()        
    return render(request, 'index.html', {'form':form})


# make with heart by Donald