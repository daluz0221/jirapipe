



from .models import Incidencias





def get_incidents(query_type):

    if query_type == "all":
        incidents = Incidencias.objects.all()
        incidents_list = []
        for incident in incidents:
            incident_dic = {
                "titulo": incident.title,
                "descripcion": incident.description,
                "progreso": incident.progress,
                "prioridad": incident.priority,
                "Fecha_limite": incident.due_date
            }

            incidents_list.append(incident_dic)

        return incidents_list