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
    # se o mapa está sendo exibido
    mapaExibido = None
    # variavel m para receber o mapa pelo plugin folium
    mapaApresentado = None
    # variavel de dados que pega demais dados!
    dadosExtraMapa = None
    # variavel do cluster de markers
    markerCluster = 0
    # variavel do tamanho do chunk
    tamanhoChunk = 200
    # se recebe um requesT POST(DO FORMULARIO/FILTRO FRONT)
    if request.method == 'POST':
        # Verifica qual a cidade selecionada na cidade
        mapaSelecionado = request.POST.get('cidade', False)
    # Se tem um mapa selecionado chegando no POST
    if mapaSelecionado is not None:
        # a cidade selecionada filtra
        mapaExibido = MapTest.objects.first()
        # se tem retorno desse código
        if mapaExibido is not None:
            # variavel m abre um mapa com as informações do mapa que deve ser exibida
            mapaApresentado = folium.Map(
                location=[mapaExibido.y, mapaExibido.x],
                zoom_start=10,
                max_native_zoom=18,
                max_zoom=20,
                tiles=' OpenStreetMap',
            )
            # define cluster para adicionar no mapa
            markerCluster = MarkerCluster().add_to(mapaApresentado)
            tooltip = "Info"
            # filtra os dados com as variveis de quant. de registros e de localização, etc
            dadosExtraMapa = MapTest.objects.all().filter(municipio='Campo Largo - PR')
            # recebe todos esses dados e separa em listas de n = 200
            dadosSeparados = [dadosExtraMapa[i::tamanhoChunk] for i in range(tamanhoChunk)]
            # para cada lista de 200
            for listaDados in dadosSeparados:
                # para cada poste dentro da lista de 200
                for poste in listaDados:
                    # cria um marker
                    folium.Marker(
                        # localização do marker a partir de poste.y e poste.x, define um tooltip e vai criar um popup
                        # com os dados do poste
                        [poste.y, poste.x], tooltip=tooltip,
                        popup=('Localização: ', poste.localizacao, 'Tipo de ponto: ', poste.tipo_de_ponto, 'Altura: ',
                               poste.altura_m, 'Esforço_DaN: ', poste.esforco_dan)
                        # adiciona ao mapa exibido
                    ).add_to(markerCluster)
        # botão fullscren
        fullscreen = Fullscreen(position='topright', title='Tela Cheia', title_cancel='Minimizar',
                                force_separate_button=True).add_to(mapaApresentado)
        # ferramenta de medida
        measure = MeasureControl(position='topleft', primary_length_unit='meters',
                                 secondary_length_unit='kilometers').add_to(mapaApresentado)
        # mapa é repassado como representação em html/javascript o que permite a visualização
        mapaApresentado = mapaApresentado._repr_html_()
    # contexto e dados repassado ao front
    context = {
        "mapas": lista,
        "mapaSelecionado": mapaSelecionado,
        "mapa": mapaApresentado,
        "dadosMapa": mapaExibido
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


@login_required(login_url='/painel/')
def newmap(request):
    return render(request, 'dashboard/newmap.html')
