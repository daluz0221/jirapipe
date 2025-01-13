



from .models import Incidencias, HistoriaUsuario





def get_incidents(query_type, user):

    if query_type == "all":
        incidents = Incidencias.objects.filter(user=user)
        incidents_list = []
        for incident in incidents:
            incident_dic = {
                "slug": incident.slug,
                "titulo": incident.title,
                "descripcion": incident.description,
                "progreso": incident.progress,
                "prioridad": incident.priority,
                "Fecha_limite": incident.due_date
            }

            incidents_list.append(incident_dic)

        return incidents_list
    

def get_history_user(query_type, incident):


    if query_type == "all":
        histories = HistoriaUsuario.objects.filter(incidencia__slug=incident)
        history_list = []
        for history in histories:
            history_dict = {
                "titulo": history.title,
                "descripcion": history.description
            }

            history_list.append(history_dict)

        return history_list