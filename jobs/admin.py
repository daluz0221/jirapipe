from django.contrib import admin

# Register your models here.
from .models import Comentarios, HistoriaUsuario, Tareas, Incidencias




admin.site.register(Comentarios)
admin.site.register(HistoriaUsuario)
admin.site.register(Tareas)
admin.site.register(Incidencias)