from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProdutoForm
from django.http import HttpResponse


from .models import Produtos

def produtolist(request):
    produto = Produtos.objects.all().order_by('-created_at')

    return render(request, 'produtos/lista.html', {'produto': produto})

def produtoView(request, id):
    produtos = get_object_or_404(Produtos, pk=id)
    return render(request, 'produtos/produto.html', {'produtos': produtos})

def adicionar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)

        if form.is_valid():
            produto = form.save(commit=False)
            produto.save()
            return redirect('/')


    form = ProdutoForm()
    return render(request, 'produtos/adicionar.html', {'form':form})


def editarProduto(request, id):
    produto = get_object_or_404(Produtos, pk=id)
    form = ProdutoForm(instance=produto)

    if(request.method == 'POST'):
        form = ProdutoForm(request.POST, instance=produto)

        if(form.is_valid()):
            produto.save()
            return redirect('/')
        else:
            return render(request, 'produtos/editarproduto.html', {'form': form, 'produto': produto})

    else:
        return render(request, 'produtos/editarproduto.html', {'form': form, 'produto' : produto})


def deletarProduto(request, id):
    produto = get_object_or_404(Produtos, pk=id)
    produto.delete()
    return redirect('/')