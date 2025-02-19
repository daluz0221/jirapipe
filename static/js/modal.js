const openModal = document.querySelector('.create_incidence');
const openModalHistory = document.querySelector('.create_history');
const openModalJob = document.querySelector('.create_job');

const modal = document.querySelector('.modal');
const closeModal = document.querySelector('.modal__close')

const openModal2 = document.querySelectorAll('.edit_incidence');
const openModalHistory2 = document.querySelectorAll('.edit_huser')
const openModalJob2 = document.querySelectorAll('.edit_tarea')

const openModal3 = document.querySelectorAll('.delete_incidence');
const openModalHistory3 = document.querySelectorAll('.delete_huser');
const openModalJob3 = document.querySelectorAll('.delete_tarea');

const modal2 = document.querySelector('#modal_edit');
const closeModal2 = document.querySelector("#close_modal");

const modal3 = document.querySelector("#delete_modal");
const closeModal3 = document.querySelector("#modal_delete_close");

if (openModal) {
    openModal.addEventListener('click', ()=>{
        modal.classList.add('modal__show')
    })
    
    closeModal.addEventListener('click', (e)=>{
        modal.classList.remove('modal__show')
    })
} 

if (openModalHistory) {
    openModalHistory.addEventListener('click', ()=>{
        modal.classList.add('modal__show')
    })
    
    closeModal.addEventListener('click', (e)=>{
        modal.classList.remove('modal__show')
    })
    
}

if (openModalJob) {
    openModalJob.addEventListener('click', ()=>{
        modal.classList.add('modal__show')
    })
    
    closeModal.addEventListener('click', (e)=>{
       
        modal.classList.remove('modal__show')
    })
}




function getIncidenceInfo(modalId, slug) {
    if (modalId == 'editar_modal' && slug) {
        fetch(`/api/incidence/${slug}`)
        .then( response => response.json() )
        .then( data =>{
            console.log(data.title);
            const title = document.querySelector('#edit__form input[name="title"]');
            const description = document.querySelector('#edit__form textarea[name="description"]');
            const priority = document.querySelector('#edit__form input[name="priority"]');
            const progress = document.querySelector('#edit__form input[name="progress"]');
            const type = document.querySelector('#edit__form #id_type');
            const dueDate = document.querySelector('#edit__form input[name="due_date"]');
            const form = document.querySelector('#edit__form');
            const formatDate = data.due_date.split('T')[0] 
            const urlForm = `incidencias/${slug}/`
            console.log(data.type);
            console.log("que impresion");
            
            
            if (title) {
                title.value = data.title !== "" ? data.title : '';
                description.value = data.description !== "" ? data.description : '';
                priority.value = data.prioridad !== "" ? data.prioridad : '';
                progress.value = data.progreso !== "" ? data.progreso : '';                
                dueDate.value = formatDate !== "" ? formatDate : '';
                type.value = data.type !== "" ? data.type : '';
                form.action = urlForm
            }else{
                console.log("no está cargando de manera correcta");
                
            }
            
        
        });     
}}

function getHistoryInfo(modalId, slug, parentSlug) {
    if (modalId == 'editar_modal' && slug) {
        fetch(`/api/history/${slug}`)
        .then( response => response.json() )
        .then( data =>{
            const title = document.querySelector('#edit__form input[name="title"]');
            const description = document.querySelector('#edit__form textarea[name="description"]');
            const estimate_time = document.querySelector('#edit__form input[name="estimate_time"]');
            const form = document.querySelector('#edit__form');
            const urlForm = `/history-user/${parentSlug}/${slug}/`
            
            if (title) {
                title.value = data.title !== "" ? data.title : '';
                description.value = data.description !== "" ? data.description : '';
                estimate_time.value = data.tiempo_estimado !== "" ? data.tiempo_estimado : "";
                form.action = urlForm

            }else{
                console.log("no está cargado de manera correcta");
                
            }
        
        });     
}}

function getJobInfo(modalId, slug, historySlug, incidenceSlug) {
    if (modalId == 'editar_modal' && slug) {
        fetch(`/api/job/${slug}`)
        .then( response => response.json() )
        .then( data =>{
            console.log(data);
            const title = document.querySelector('#edit__form input[name="title"]');
            const description = document.querySelector('#edit__form textarea[name="description"]');
            const state = document.querySelector('#edit__form #id_state');
            const form = document.querySelector('#edit__form');
            const urlForm = `/job/${incidenceSlug}/${historySlug}/${slug}/`

            if (title) {
                title.value = data.title !== "" ? data.title : '';
                description.value = data.description !== "" ? data.description : '';
                state.value = data.state !== "" ? data.state : "";
                form.action = urlForm

            }else{
                console.log("no está cargado de manera correcta");
                
            }
        });     
}}



if(openModal2){
    openModal2.forEach( but =>{
        but.addEventListener('click', (event)=>{
        
            const slug = but.getAttribute("data-slug")
            
            
        
            modal2.classList.add('modal__show')
            getIncidenceInfo('editar_modal', slug)    
        })
    } )    
}





if(openModalHistory2){
    openModalHistory2.forEach( but =>{
        but.addEventListener('click', ()=>{
            const historySlug = but.getAttribute("data-history-slug");
            const incidenceSlug = but.getAttribute("data-incidence-slug");
            
    
            modal2.classList.add('modal__show')
            getHistoryInfo('editar_modal', historySlug, incidenceSlug)
        })
        
    })
    
}


if (openModalJob2) {
    openModalJob2.forEach( but =>{

        but.addEventListener('click', ()=>{
            
            const jobSlug = but.getAttribute("data-job-slug")
            const historySlug = but.getAttribute("data-history-slug");
            const incidenceSlug = but.getAttribute("data-incidence-slug");
           
    
            modal2.classList.add('modal__show')
            getJobInfo('editar_modal', jobSlug, historySlug, incidenceSlug)
        })
    
    }) 
}






closeModal2.addEventListener('click', (e)=>{
    console.log("test");
    
    modal2.classList.remove('modal__show')
})

if (openModal3) {
    openModal3.forEach( but =>{
        but.addEventListener('click', (e)=>{
            modal3.classList.add('modal__show')
            const text = document.querySelector("#delete_modal h2")
            const title = but.getAttribute("data-title")
            const slug = but.getAttribute("data-slug")
      
            text.innerHTML = "¿Realmente desea eliminar " + title + " ?"
    
            const form = document.querySelector("#delete_form");
            const urlform = `delete/Incidencias/${slug}/` 
    
            form.action = urlform
    
        })
    }) 
}


if(openModalHistory3){
    openModalHistory3.forEach( but =>{
        but.addEventListener('click', (e)=>{
            modal3.classList.add('modal__show')
            const text = document.querySelector("#delete_modal h2")
            const slug = but.getAttribute("data-slug");
            const title = but.getAttribute("data-title");
    
            text.innerHTML = "¿Realmente desea eliminar " + title + " ?"
            const form = document.querySelector("#delete_form");
            const urlform = `delete/HistoriaUsuario/${slug}/` 
            form.action = window.location.origin + "/" +  urlform
    
        })
    } )
    
}


if (openModalJob3) {
    openModalJob3.forEach( but =>{
        but.addEventListener('click', (e)=>{
            modal3.classList.add('modal__show')
            const text = document.querySelector("#delete_modal h2")
            const slug = but.getAttribute("data-slug");
            const title = but.getAttribute("data-title");
    
            text.innerHTML = "¿Realmente desea eliminar " + title + " ?"
            const form = document.querySelector("#delete_form");
            const urlform = `delete/Tareas/${slug}/` 
            form.action = window.location.origin + "/" +  urlform
    
        })
    } )
     
}


closeModal3.addEventListener("click", (e)=>{
    console.log("llego");
    e.preventDefault()

    
    modal3.classList.remove('modal__show');

})