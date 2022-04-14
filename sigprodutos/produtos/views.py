from pickle import TRUE
from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
def index(request):
    produtos = Produto.objects.all()
    return render(request,"index.html",{'produtos':produtos})
def new(request):
    new = TRUE
    return render(request,"form.html", {'new': new})
def store(request):
    produto = ProdutoForm()
    if request.method == "POST":
        produto= ProdutoForm(request.POST)
        if(produto.is_valid()):
            produto.save()
    return redirect('/produtos/index')
def update(request):
    return redirect('/produtos/index')
def edit(request,id):
    new = False
    produto = Produto.objects.get(id=id)
    if(produto != None):
        return render(request,"form.html", {'new': new, 'produto':produto})
    else:
        return redirect('/produtos/index')

def delete(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return render(request,"index.html")