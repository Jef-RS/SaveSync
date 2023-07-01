const documents = document.querySelector('#folderInput');
const selectFiles = document.querySelector('.main__games__plus__icon');
let fileValue = document.querySelector('#fileValue');

selectFiles.addEventListener('click', () => {
    documents.click();
})

documents.addEventListener('change', (evento) => {
    const files = evento.target.files;

    for(var i = 0; i < files.length; i++) {
        console.log(files[i].path)
        fileValue.innerHTML += files[i].path;
    }
})