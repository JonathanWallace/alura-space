from django.urls import path
from apps.galeria.views import index, imagem, buscar, nova_foto, editar_foto, deletar_foto, filtro

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:id_foto>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('filtro/<str:filtro>', filtro, name='filtro'),
    path('nova-imagem', nova_foto, name='nova-imagem'),
    path('editar-imagem/<int:id_foto>', editar_foto, name='editar-imagem'),
    path('deletar-imagem/<int:id_foto>', deletar_foto, name='deletar-imagem')
]
