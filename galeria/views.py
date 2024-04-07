from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.filter(publicado=True)
    return render(request, 'galeria\index.html', {'cards': fotografias})

def imagem(request, id_foto):
    fotografia = get_object_or_404(Fotografia, pk=id_foto)
    return render(request, 'galeria\imagem.html', {'fotografia': fotografia})