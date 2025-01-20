from django import forms


from .models import Incidencias, HistoriaUsuario, Tareas



class IncidenciaForm(forms.ModelForm):

    class Meta:
        model = Incidencias
        fields = (
            'title',
            'description',
            'type',
            'priority',
            'due_date'
        )

        widgets = {
            'due_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            )
        }



class HistoryUserForm(forms.ModelForm):

    class Meta:
        model = HistoriaUsuario
        fields = (
            'title',
            'description',
            'estimate_time'
        )

     


