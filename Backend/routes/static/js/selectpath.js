export const gameList = document.querySelector('.main__profile__options');

export function SelectPath() {
    const documents = document.querySelector('#folderInput');
    const selectFiles = document.querySelector('.main__games__plus__icon');
    
    
    let fileValue = document.querySelector('#fileValue');

    selectFiles.addEventListener('click', () => {
        documents.click();
    })
    
    documents.addEventListener('change', (evento) => {
        const files = evento.target.files;
        console.log(files[0].webkitRelativePath)
    
        // Adiciona o nome do arquivo na barra lateral
        const currentPath = files[0].webkitRelativePath;
        const pathName = currentPath.slice(0, currentPath.indexOf('/'));
        let createList = document.createElement('a');

        createList.classList.add('main__profile__items', 'hover');
        createList.innerHTML = pathName;
        gameList.appendChild(createList);
    
        for(var i = 0; i < files.length; i++) {
            console.log(files[i].path)
            // Lista todos os arquivos que estao dentro da pasta principal
            fileValue.innerHTML += files[i].path;
        }
    })
}