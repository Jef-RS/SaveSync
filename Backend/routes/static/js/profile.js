export function Profile() {
    const profile = document.querySelector(".header__profile");
    const aside = document.querySelector('.main__profile__content');

    let isValid = true;
    
    profile.addEventListener('click', () => {
        if(isValid) {
            aside.style.display = "none";
            isValid = false;
        }else{
            aside.style.display = "flex";
            isValid = true
        }
    })
}