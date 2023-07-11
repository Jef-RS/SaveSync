import { Profile } from "./profile.js";
import { SelectPath, gameList } from "./selectpath.js";

function RenderContent() {
    const asideContent = document.querySelector('.main__games__content');
    
    
    const content = `
        <h2 class="main__games__select__title">Please, select your path.</h2>
        <div class="main__games__icon__container hover">
        <img class="main__games__plus__icon" src="../static/images/plus.svg" alt="select path">
        </div>
        <p style="overflow-x: hidden;" id="fileValue">...</p>
        <input class="main__games__select__file" type="file" id="folderInput" webkitdirectory directory multiple>
    `

    function AsideContentRender(content) {
        const containerContent = `
        <div class="main__games__select__container">
        ${content}
        </div>
        `
        return containerContent;
    }
        
    asideContent.innerHTML = AsideContentRender(content);
    
    gameList.addEventListener('click', () => {
        asideContent.innerHTML = AsideContentRender(`
            <img onClick=" window.location.href = '/home' " class="main__games__back__arrow hover" src="../static/images/back_arrow.svg" />
            <img style="width: 128px; margin: auto" src="https://cdn.cloudflare.steamstatic.com/steam/apps/730/capsule_616x353.jpg?t=1585694942" />
        `);
    });

    return  (
        Profile(),
        SelectPath()
    )
}

RenderContent();