from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import auth

def login(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')

    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("index")
            else:
                msg = 'Acesso inválido! ''Usuário ou Senha incorretos.'
        else:
            msg = 'Erro ao validar o formulário'
    return render(request, "contas/login.html", {"form": form, "msg": msg})

def logout(request):
    """Realiza logout do usuário"""
    auth.logout(request)
    return redirect('login')
