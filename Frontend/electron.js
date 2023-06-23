const { app, BrowserWindow } = require('electron');
const path = require('path');
const { spawn } = require('child_process');



let mainWindow;
let flaskProcess; // Variável para armazenar a referência do processo Flask

function createWindow() {
  // Iniciar o servidor Flask
  const backend_path = '/home/anderson/Projetos/SaveSync/Backend/routes/app.py';
  const flaskScriptPath = path.join(backend_path);
  flaskProcess = spawn('python', [flaskScriptPath]);

  flaskProcess.stdout.on('data', (data) => {
    console.log(`Servidor Flask: ${data}`);
  });

  flaskProcess.stderr.on('data', (data) => {
    console.error(` Flask: ${data}`);
  });


  // Criar a janela do Electron
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: false
    }
  });
  

  // Carregar o servidor Flask no Electron
  mainWindow.loadURL('http://localhost:5000');
  
  

  mainWindow.on('closed', function () {
    // Fechar a janela do Electron e encerrar o processo Flask
    mainWindow = null;
    if (flaskProcess) {
      flaskProcess.kill();
    }
  });
}

app.on('ready', () => {
  createWindow();
  // Configurar o electron-reload para monitorar alterações nos arquivos do aplicativo

});

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', function () {
  if (mainWindow === null) {
    createWindow();
    app.relaunch()
  }
 
});


  