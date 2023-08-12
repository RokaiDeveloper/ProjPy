from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import folium
import pandas as pd
from folium.plugins import MarkerCluster, Fullscreen, MeasureControl
from app.models import AppUserMaps, MapTest, MapaOficial


# Create your views here.
def home(request):
    return render(request, 'home.html')


# validação e do cadastro
def store(request):
    data = {}
    if request.POST['password'] != request.POST['password-conf']:
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        user.user_permissions.add()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request, 'create.html', data)


# criação de usuario
def create(request):
    return render(request, 'create.html')


# Painel de Login
def painel(request):
    return render(request, 'painel.html')


# Processamento do login e autenticação
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)


# precisa estar logado
@login_required(login_url='/painel/')
# acessa home do usuario
def dashboard(request):
    return render(request, 'dashboard/home.html')


# redirect para um logouts
def logouts(request):
    logout(request)
    return redirect('/home/')


# mapa
@login_required(login_url='/painel/')
def map(request):
    # Recebe todos os mapas disponiveis para o usuario logado
    mapas = AppUserMaps.objects.select_related().filter(user=request.user.id).values_list('map__nome_cidade')
    # lista para poder iterar posteriormente no front
    lista = list(mapas)
    # declarações das variaveis vazias para utilização posterior
    # mapa selecionado
    mapaSelecionado = None

    context = {
        "mapas": lista,
        "mapaSelecionado": mapaSelecionado
    }

    return render(request, 'dashboard/map.html', context)


# perfil do usuario
@login_required(login_url='/painel/')
def perfil(request):
    # Recebe todos os mapas disponiveis para o usuario logado
    mapas = AppUserMaps.objects.select_related().filter(user=request.user.id).values_list('map__nome_cidade')
    # lista para poder iterar posteriormente no front
    lista = list(mapas)
    context = {
        "mapas": lista
    }
    return render(request, 'dashboard/perfil.html', context)

