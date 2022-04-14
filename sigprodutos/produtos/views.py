from django.shortcuts import render, redirect
from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    return render(request,"index.html",{'produtos':produtos})
def new(request):
    return render(request,"index.html")
def store(request):
    return render(request,"index.html")
def update(request):
    return render(request,"index.html")
def edit(request,id):
    return render(request,"index.html")
def delete(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return render(request,"index.html")