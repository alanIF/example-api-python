from django.shortcuts import render, redirect
from .models import Tarefa

def index(request):
    tarefas = Tarefa.objects.all()
    return render(request,"index.html",{'tarefas':tarefas})
def destroy(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()
    return render(request,"index.html")