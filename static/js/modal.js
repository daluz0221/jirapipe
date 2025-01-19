const openModal = document.querySelector('.create_incidence');
const modal = document.querySelector('.modal');
const closeModal = document.querySelector('.modal__close')

openModal.addEventListener('click', ()=>{
    modal.classList.add('modal__show')
})

closeModal.addEventListener('click', ()=>{
    modal.classList.remove('modal__show')
})