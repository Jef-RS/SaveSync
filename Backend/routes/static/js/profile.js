const perfil = document.querySelector(".header__profile");
const aside = document.querySelector('.main__profile__content');
const cards = document.querySelectorAll(".main__games__content");



let isValid = true;

perfil.addEventListener('click', () => {
    if(isValid) {
        aside.style.display = "none";
        isValid = false;
    }else{
        aside.style.display = "flex";
        isValid = true
    }
})