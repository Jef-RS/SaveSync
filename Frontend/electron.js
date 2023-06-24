const { app, BrowserWindow } = require('electron');
const path = require('path');
const { spawn } = require('child_process');
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

const appPath = path.join(__dirname, '/');

let mainWindow;
let flaskProcess;

function createWindow() {
  let backendPath;
  let flaskScriptPath;

  if (process.platform === 'win32') {
    backendPath = directories.dirFrontendRoutes;
    flaskScriptPath = path.join(backendPath);
    flaskProcess = spawn('python', [flaskScriptPath]);
  } else if (process.platform === 'linux') {
    backendPath = '/Projetos/SaveSync/Backend/routes/app.py';
    flaskScriptPath = path.join(backendPath);
    flaskProcess = spawn('python3', [flaskScriptPath]);
  } else {
    throw new Error('Plataforma não suportada.');
  }

  flaskProcess.stdout.on('data', (data) => {
    console.log(`Servidor Flask: ${data}`);
  });

  flaskProcess.stderr.on('data', (data) => {
    console.error(`Flask: ${data}`);
  });

  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js')
    }
  });

  mainWindow.loadURL('http://localhost:5000');

  mainWindow.on('closed', function () {
    mainWindow = null;
    if (flaskProcess) {
      flaskProcess.kill();
    }
  });
}

app.on('ready', () => {
  createWindow();
});

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', function () {
  if (mainWindow === null) {
    createWindow();
  }
});
