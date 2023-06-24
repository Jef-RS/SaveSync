const path = require('path');
const os = require('os');

function getDirectories() {
  const directory = __dirname;
  const nameArq = path.basename(directory);
  const rootDirectory = directory.slice(0, -'Backend/r'.length);

  const dirAbSp = rootDirectory;
  const dirFrontendRoutes = path.join(dirAbSp, 'Backend/routes/app.py');
  const dirFrontendStatic = path.join(dirAbSp, 'Frontend/static');

  return {
    directory,
    nameArq,
    rootDirectory,
    dirAbSp,
    dirFrontendRoutes,
    dirFrontendStatic
  };
}

// Exemplo de uso
const directories = getDirectories();
console.log(directories.dirFrontendRoutes);
