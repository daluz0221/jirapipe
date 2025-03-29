const wrapper = document.querySelector('.wrapper');
const registerLink = document.querySelector('.register_link');
const loginLink = document.querySelector('.login_link');

registerLink.addEventListener('click', ()=>{
    wrapper.classList.add('active');
    
})

loginLink.addEventListener('click', ()=>{
    wrapper.classList.remove('active');
    
})