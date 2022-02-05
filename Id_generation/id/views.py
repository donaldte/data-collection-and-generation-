
from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from .forms import ProfileForm, UserForm
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, View





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
@login_required
def success(request):
    return render(request, 'success.html')        

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def search(request, *args, **kwargs):
    nui = request.GET.get('nui')
    if nui !='' and nui is not None:
       
        recherche = UserProfile.objects.get(identification__icontains=nui)
         
                  
        if recherche:
            message = "the nui you have entered exist"
        else:
            message = "the nui you have entered does not existe" 
        return render(request, 'search.html', {'message':message})   
    else:
        message = ''
        return render(request, 'search.html', {'message':message})         

# Create your views here.
# This function will help to valid data and save()
# def create(request, *args, **kwargs):
#     "cette methode n'est pas tres approprie mais je veux juste que tu puisse comprendre on pouvais faire court en utilisant le view ou le formview"
#     if request.method == "POST":
#         name = request.POST.get('name')
#         username = request.POST.get('username')
#         date = request.POST.get('date')
#         place = request.POST.get('place')
#         email = request.POST.get('email')
#         pwd = request.POST.get('pwd')
#         repwd = request.POST.get('repwd')
#         status = request.POST.get('status')
#         sex = request.POST.get('sex')
#         matrial = request.POST.get('matrial')
#         activite = request.POST.get('activite')
#         NomDeLaMere = request.POST.get('NomDeLaMere')
#         PrenomDeLaMere = request.POST.get('PrenomDeLaMere')
#         NomDuPere = request.POST.get('NomDuPere')
#         PrenomDuPere = request.POST.get('PrenomDuPere')
#         pays = request.POST.get('pays')
#         ville = request.POST.get('ville')
#         ndd = request.POST.get('ndd')
#         ddlIDCOMMUNE2 = request.POST.get('ddlIDCOMMUNE2')
#         txtCOMMUNE2 = request.POST.get('txtCOMMUNE2')
#         quatier = request.POST.get('quatier')
#         Lieu_dit = request.POST.get('Lieu_dit')
#         Unite_de_gestion  = request.POST.get('Unite_de_gestion')
#         tel = request.POST.get('tel')
#         if pwd == repwd:
#             a = make_password(pwd)
#             data = UserProfile.objects.create(name=name, username=username, date=date, place=place, email=email, pwd=a, status=status, sex=sex, matrial=matrial, activite=activite, NomDeLaMere=NomDeLaMere, PrenomDeLaMere=PrenomDeLaMere, NomDuPere=NomDuPere, PrenomDuPere=PrenomDuPere, pays=pays, ville=ville, ndd=ndd, ddlIDCOMMUNE2=ddlIDCOMMUNE2,txtCOMMUNE2=txtCOMMUNE2, quatier=quatier, Lieu_dit=Lieu_dit, Unite_de_gestion=Unite_de_gestion, tel=tel)


#             messages.success(request, 'Data was successfully save....thank')
#             form = ProfileForm()
#             object = UserProfile.objects.all()
#             long = len(object)
#             id = object[long-1]
#             return render(request, 'index.html', {'form':form, 'object':id})

#         else:
#             messages.error(request, "passwords doesn't match")
            
           
#     return render(request, 'registration.html')


# This method is very good 
class Create(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration.html')

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                data = form.save(commit=False)
                pw = request.POST.get('pwd')
                pwr = request.POST.get('repwd')
                if pw == pwr:    
                    data.pwd = make_password(pw)
                    data.save()
                    messages.success(request, 'Data was successfully save....thank')
                    form = ProfileForm()
                    object = UserProfile.objects.all()
                    long = len(object)
                    id = object[long-1]
                    return render(request, 'index.html', {'form':form, 'object':id})
                else:
                    messages.error(request, 'password does not match')
                    return render(request, 'index.html', {'form':form})


            else:
                return render(request, 'index.html', {'form':form})    
    
# make with heart by Donald