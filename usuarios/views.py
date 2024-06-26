from django.http import HttpResponse
from django.shortcuts import render 
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib import messages

@has_permission_decorator('cadastrar_catador')
def cadastrar_catador(request):
    if request.method == "GET":
        catadores = Users.objects.filter(permissao="C")
        return render(request, 'cadastrar_catador.html', { 'catadores': catadores })

    if request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        #TODO: Fazer validações dos dados
        user = Users.objects.filter(email=email)

        if user.exists():
            messages.add_message(request, messages.SUCCESS, 'Email já cadastrado no Sistema!!!')
            return redirect(reverse('cadastrar_catador'))
        
        user = Users.objects.create_user(username=email, email=email, password=senha, first_name=nome, last_name=sobrenome, permissao="C")

        messages.add_message(request, messages.SUCCESS, 'Catador cadastrado com sucesso!!!')
    return redirect(reverse('cadastrar_catador'))
def login(request):
    if request.method == "GET":
        if request.Users.is_authenticated:
            return redirect(reverse('plataforma'))
        return render(request, 'login.html')
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)

        if not user:
            messages.add_message(request, messages.SUCCESS, 'Usuário Inválido!!!')
            return redirect(reverse('cadastrar_catador'))
        
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Usuário Logado com Sucesso!!!')
            return redirect(reverse('cadastrar_catador'))
def logout(request):
    request.session.flush()
    return redirect(reverse('login'))

@has_permission_decorator('cadastrar_catador')
def excluir_usuario(request, id):
    catador =get_object_or_404(Users, id=id)
    catador.delete()
    messages.add_message(request, messages.SUCCESS, 'Catador excluido com sucesso!!!')
    return redirect(reverse('cadastrar_catador'))