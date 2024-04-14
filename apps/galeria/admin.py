from django.contrib import admin
from apps.galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id','nome','legenda', 'publicado')
    list_display_links = ('id','nome')
    search_fields = ('id','nome')
    list_filter = ('categoria',)
    list_editable = ['publicado']
    list_per_page = 20
admin.site.register(Fotografia, ListandoFotografias)