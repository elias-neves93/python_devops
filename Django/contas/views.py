from django.shortcuts import render, redirect
from .models import Transacao
from .forms import TransacaoForm
# Create your views here.

from django.http import HttpResponse
import datetime

def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()
    #html = "<html><body> It is now {} </body> </html>".format(now)
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listagem')

    data['form'] = form
    return render(request, 'contas/form.html', data)
