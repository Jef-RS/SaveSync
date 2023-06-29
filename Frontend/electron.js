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


const directories = getDirectories();

const appPath = path.join(__dirname, '/');

let mainWindow;
let flaskProcess;

function createWindow() {
  let backendPath;
  let flaskScriptPath;
  let isReloaded = false;

  if (process.platform === 'win32') {
    backendPath = directories.dirFrontendRoutes;
    flaskScriptPath = path.join(backendPath);
    flaskProcess = spawn('python', [flaskScriptPath]);
  } else if (process.platform === 'linux') {
    backendPath = directories.dirFrontendRoutes;
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
    autoHideMenuBar: true,
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
  mainWindow.webContents.on('did-finish-load', () => {
    if (!isReloaded) {
      mainWindow.reload(); // Faz o reload da página apenas na primeira vez
      isReloaded = true; // Define a variável isReloaded como true para evitar mais reloads
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

