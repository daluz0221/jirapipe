const openModal = document.querySelector('.create_incidence');
const openModalHistory = document.querySelector('.create_history');
const openModalJob = document.querySelector('.create_job');

const modal = document.querySelector('.modal');
const closeModal = document.querySelector('.modal__close')

const openModal2 = document.querySelectorAll('.edit_incidence');

const openModalHistory2 = document.querySelectorAll('.edit_huser')


const modal2 = document.querySelector('#modal_edit');
const closeModal2 = document.querySelector("#close_modal");

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
            console.log(data);
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


openModal2.forEach( but =>{
    but.addEventListener('click', (event)=>{
    
        const slug = but.getAttribute("data-slug")
        
        
    
        modal2.classList.add('modal__show')
        getIncidenceInfo('editar_modal', slug)    
    })
} )




openModalHistory2.forEach( but =>{
    but.addEventListener('click', ()=>{
        const historySlug = but.getAttribute("data-history-slug");
        const incidenceSlug = but.getAttribute("data-incidence-slug");
        console.log(historySlug);
        console.log(incidenceSlug);

        modal2.classList.add('modal__show')
        getHistoryInfo('editar_modal', historySlug, incidenceSlug)
    })
    
})







closeModal2.addEventListener('click', (e)=>{
    modal2.classList.remove('modal__show')
})