const not_register = document.querySelector('.not_register');
const not_add = document.querySelector('.not_add');

not_register.addEventListener('click', () => {
    alert('You must be admin to register an item')
});

not_add.addEventListener('click', () => {
    alert('You must be admin to add an item')
});