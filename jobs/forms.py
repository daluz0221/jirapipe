from django import forms


from .models import Incidencias, HistoriaUsuario, Tareas



class IncidenciaForm(forms.ModelForm):

    class Meta:
        model = Incidencias
        fields = '__all__'