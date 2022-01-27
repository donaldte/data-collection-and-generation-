from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import ProfileForm


# Create your views here.
# This function will help to valid data and save()
def create(request, *args, **kwargs):
    if request.method == "POST":
        form = ProfileForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data was successfully save....thank')
            return redirect("/")
        else:
            form = ProfileForm(data=request.POST)
            messages.error(request, form.errors)
            return redirect("/")
    else:
        form = ProfileForm()        
    return render(request, 'index.html', {'form':form})


# make with heart by Donald