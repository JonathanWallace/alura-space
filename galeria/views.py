from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.order_by('-nome').filter(publicado=True)
    return render(request, 'galeria\index.html', {'cards': fotografias})

def imagem(request, id_foto):
    fotografia = get_object_or_404(Fotografia, pk=id_foto)
    return render(request, 'galeria\imagem.html', {'fotografia': fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by('-nome').filter(publicado=True)
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, 'galeria\\buscar.html', {'cards': fotografias})