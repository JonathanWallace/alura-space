from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia
from django.contrib import messages

def validador(func):
    def verificar(*args, **kwargs):
        if not args[0].user.is_authenticated:
            messages.error(args[0], f'Você precisa estar logado!')
            return redirect('login')
        else:
            return func(*args,**kwargs)
    return verificar

@validador
def index(request):
    fotografias = Fotografia.objects.order_by('-nome').filter(publicado=True, usuario=request.user)
    return render(request, 'galeria\index.html', {'cards': fotografias})

@validador
def imagem(request, id_foto):
    fotografia = get_object_or_404(Fotografia, pk=id_foto)
    return render(request, 'galeria\imagem.html', {'fotografia': fotografia})

@validador
def buscar(request):
    fotografias = Fotografia.objects.order_by('-nome').filter(publicado=True, usuario=request.user)
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, 'galeria\\buscar.html', {'cards': fotografias})