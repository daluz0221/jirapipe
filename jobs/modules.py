



from .models import Incidencias, HistoriaUsuario, Tareas





def get_incidents(query_type, user, **kwargs):

    if query_type == "all":
        incidents = Incidencias.objects.filter(user=user, is_delete=False)
        incidents_list = []
        for incident in incidents:
            incident_dic = {
                "slug": incident.slug,
                "titulo": incident.title,
                "descripcion": incident.description,
                "progreso": incident.progress,
                "prioridad": incident.priority,
                "Fecha_limite": incident.due_date,
                "tipo": incident.type
            }

            incidents_list.append(incident_dic)

        return incidents_list
    
    if query_type == "one":
        
        slug_incidence = kwargs.get("slug")
        incidence = Incidencias.objects.get(slug=slug_incidence)
        if incidence.is_delete:
            return "not found"

        return incidence
        
    

def get_history_user(query_type, **kwargs):

    if query_type == "home":
        try:
            husers = HistoriaUsuario.objects.filter(is_delete=False)
        except:
            husers = []

        return husers


    if query_type == "all":
        try:
            incident_slug = kwargs.get("incident_slug")
            incidencia = Incidencias.objects.get(slug=incident_slug)
            if incidencia.is_delete:
                return "not found"
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
        
        histories = HistoriaUsuario.objects.filter(incidencia__slug=incident_slug, is_delete=False)
        history_list = []
        for history in histories:
            history_dict = {
                "titulo": history.title,
                "descripcion": history.description,
                "slug": history.slug
            }

            history_list.append(history_dict)

        return {"history_list": history_list, "incidencia_dict": incidencia_dict}
    

    if query_type == "one":
        
        try:
            hsuer_slug = kwargs.get("histoy_user_slug")
            huser = HistoriaUsuario.objects.get(slug=hsuer_slug)
               
        except HistoriaUsuario.DoesNotExist:
            huser = None

        return huser
    
def get_tareas(query_type, **kwargs):

    if query_type == "home":
        try:
            tareas = Tareas.objects.filter(is_delete=False)
        except:
            tareas = []

        return tareas


    if query_type == "all":
        try:
            history_user_slug = kwargs.get("history_user_slug")
            history_user = HistoriaUsuario.objects.get(slug=history_user_slug)
            if history_user.is_delete:
                return "not found"
            history_user_dict = {
                "titulo": history_user.title,
                "descripcion": history_user.description,
                "slug": history_user.slug
            }
        except HistoriaUsuario.DoesNotExist:
            history_user_dict = {}

        tareas = Tareas.objects.filter(user_history__slug=history_user_slug, is_delete=False)
        tareas_list = []
        for tarea in tareas:
            tarea_dict = {
                "titulo": tarea.title,
                "slug": tarea.slug,
                "descripcion": tarea.description,
                "estado": tarea.state,
            }
            tareas_list.append(tarea_dict)


        return {
            "history_user_dict": history_user_dict,
            "tareas_list": tareas_list
        }



