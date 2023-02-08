const btn_close = document.querySelector('.btn-close');
const message_flash = document.querySelector('.message_flash')

btn_close.addEventListener('click', () => {
    message_flash.classList.add('close')
});