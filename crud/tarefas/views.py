from django.shortcuts import render, redirect
from .models import Tarefa

def index(request):
    tarefas = Tarefa.objects.all()
    return render(request,"index.html",{'tarefas':tarefas})
