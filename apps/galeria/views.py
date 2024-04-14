from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages
from apps.galeria.forms import FotoForms

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
    
    fotografia = get_object_or_404(Fotografia, pk=id_foto, usuario_id=request.user.id)
    return render(request, 'galeria\imagem.html', {'fotografia': fotografia})

@validador
def buscar(request):
    fotografias = Fotografia.objects.order_by('-nome').filter(publicado=True, usuario=request.user)
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, 'galeria/index.html', {'cards': fotografias})

@validador
def filtro(request, filtro):
    fotografias = Fotografia.objects.order_by('-nome').filter(publicado=True, usuario=request.user, categoria=filtro)
    return render(request, 'galeria/index.html', {'cards': fotografias})

@validador
def nova_foto(request):
    form = FotoForms()
    if request.method == 'POST':
        form = FotoForms(request.POST, request.FILES)  
        
        if form.is_valid():       
            fotografia = Fotografia.objects.get(pk=form.save().id)
            fotografia.usuario = request.user
            fotografia.save()
            messages.success(request, "Nova fotografia cadastrada")
            return redirect('index')
    return render(request, 'galeria/nova-imagem.html', {'form' : form})

@validador
def editar_foto(request, id_foto):
    fotografia = Fotografia.objects.get(id=id_foto,usuario_id=request.user.id)
    form = FotoForms(instance=fotografia)

    if request.method == 'POST':
        form = FotoForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, f"Fotografia: {form['nome'].value()} editada com sucesso")
            return redirect('index')

    return render(request, 'galeria/editar-imagem.html', {"form" : form, 'id_foto':id_foto})

@validador
def deletar_foto(request, id_foto):
    fotografia = Fotografia.objects.get(id=id_foto,usuario_id=request.user.id)
    fotografia.delete()
    messages.success(request, f"Fotografia:{fotografia.nome} excluida com sucesso!")
    return redirect('index')
