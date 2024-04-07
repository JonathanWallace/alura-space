from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id','nome','legenda','publicado')
    list_display_links = ('id','nome')
    search_fields = ('id','nome')
    list_filter = ('categoria', 'publicado')
    list_per_page = 20
admin.site.register(Fotografia, ListandoFotografias)