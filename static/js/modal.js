const openModal = document.querySelector('.create_incidence');
const modal = document.querySelector('.modal');
const closeModal = document.querySelector('.modal__close')

const openModal2 = document.querySelectorAll('.edit_incidence');
const modal2 = document.querySelector('#modal_edit');
const closeModal2 = document.querySelector("#close_modal");


openModal.addEventListener('click', ()=>{
    modal.classList.add('modal__show')
})

closeModal.addEventListener('click', (e)=>{
   
    modal.classList.remove('modal__show')
})

function getInfo(modalId, slug) {
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

console.log(typeof openModal2);


openModal2.forEach( but =>{
    but.addEventListener('click', (event)=>{
    
        const slug = but.getAttribute("data-slug");
        console.log(slug);
        
    
        modal2.classList.add('modal__show')
        getInfo('editar_modal', slug)
        
    
        
        
    })
} )

closeModal2.addEventListener('click', (e)=>{
   
    modal2.classList.remove('modal__show')
})