



from .models import Incidencias, HistoriaUsuario, Tareas





def get_incidents(query_type, user, **kwargs):

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
    
    if query_type == "one":
        
        slug_incidence = kwargs.get("slug")
        incidence = Incidencias.objects.get(slug=slug_incidence)
        

        return incidence
        
    

def get_history_user(query_type, incident_slug):


    if query_type == "all":
        try:
            incidencia = Incidencias.objects.get(slug=incident_slug)
            incidencia_dict = {
                "slug": incidencia.slug,
                "titulo": incidencia.title,
                "descripcion": incidencia.description,
                "progreso": incidencia.progress,
                "prioridad": incidencia.priority,
                "Fecha_limite": incidencia.due_date
            } 
        except Incidencias.DoesNotExist:
            incidencia_dict = {}
        histories = HistoriaUsuario.objects.filter(incidencia__slug=incident_slug)
        history_list = []
        for history in histories:
            history_dict = {
                "titulo": history.title,
                "descripcion": history.description,
                "slug": history.slug
            }

            history_list.append(history_dict)

        return {"history_list": history_list, "incidencia_dict": incidencia_dict}
    
def get_tareas(query_type, history_user_slug):


    if query_type == "all":
        try:
            history_user = HistoriaUsuario.objects.get(slug=history_user_slug)
            history_user_dict = {
                "titulo": history_user.title,
                "descripcion": history_user.description
            }
        except HistoriaUsuario.DoesNotExist:
            history_user_dict = {}

        tareas = Tareas.objects.filter(user_history__slug=history_user_slug)
        tareas_list = []
        for tarea in tareas:
            tarea_dict = {
                "titulo": tarea.title,
                "descripcion": tarea.description,
                "estado": tarea.state
            }
            tareas_list.append(tarea_dict)


        return {
            "history_user_dict": history_user_dict,
            "tareas_list": tareas_list
        }



