from django.shortcuts import render
from django.shortcuts import redirect
from rajim.models import *
from django.template import loader, Context, RequestContext
from .forms import *
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def Album(request,id_disco):
    disco = Disco.objects.get(id_disco=id_disco)
    comentarios = ComentaDisco()
    form = SurveyForm()
   
    return render(request,'rajim/Disco.html',{'disco':disco,'form':form},context_instance=RequestContext(request))
def BusquedaAlbum(request):
    discos = Disco.objects.filter(status=True)
    return render(request,'rajim/BusquedaDisco.html',{'discos':discos},context_instance=RequestContext(request))

def Contacto(request):
    return render(request,'rajim/Contacto.html',{})
def Registrar(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
        if request.method == "POST":
            form= RegisterForm(request.POST)
            if form.is_valid():
                usuario = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password_one = form.cleaned_data['password_one']
                password_two = form.cleaned_data['password_two']
                u = User.objects.create_user(username=usuario, email=email,password=password_one)
                u.save()
                return render(request,'rajim/Registrar2.html',context_instance=RequestContext(request))
            else:
                return render(request,'rajim/Registrar.html',{'form':form},context_instance=RequestContext(request))

        return render(request,'rajim/Registrar.html',{'form':form},context_instance=RequestContext(request))

def Ingresar(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect('/')
                else:
                    mensaje = "usuario y/o password incorrecto"
        form = LoginForm()
        return render(request,'rajim/Ingresar.html',{'form':form, 'mensaje':mensaje},context_instance=RequestContext(request))

def CerrarSesion(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def Ranking(request):
    rankartista = Artista.objects.filter(valoracion_artista__isnull=False).order_by('-valoracion_artista')
    rankdisco = Disco.objects.filter(valoracion_disco__isnull=False).order_by('-valoracion_disco')
    rankuser = userProfile.objects.filter(valoracion_user__isnull=False).order_by('-valoracion_user')
    return render(request,'rajim/Ranking.html',{'rankartista':rankartista, 'rankdisco':rankdisco, 'rankuser':rankuser})
def Registrar2(request):
    return render(request, 'rajim/Registrar2.html',{})
def Perfil(request):
    if request.user.is_authenticated():
        return render(request, 'rajim/Perfil.html',{})

    else:
        return HttpResponseRedirect('/')

    return render(request, 'rajim/Perfil.html',{})

def EditarPerfil(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            # formulario enviado
            user_form = UserForm(request.POST, instance=request.user)
            perfil_form = PerfilForm(request.POST, request.FILES, instance=request.user.profile)
            if user_form.is_valid() and perfil_form.is_valid():
                # formulario validado correctamente
                user_form.save()
                perfil_form.save()
                return HttpResponseRedirect('/rajim/Perfil.html')

        else:
            # formulario inicial
            user_form = UserForm(instance=request.user)
            perfil_form = PerfilForm(instance=request.user.profile)
        return render(request,'rajim/EditarPerfil.html', { 'user_form': user_form,  'perfil_form': perfil_form }, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')





