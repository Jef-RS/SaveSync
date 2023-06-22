const { app, BrowserWindow, ipcMain } = require('electron');
const isDev = require('electron-is-dev');
const path = require('path');
const Store = require('electron-store');

const store = new Store();

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: false,
    },
  });

  const serverProcess = spawn('python', ['server.py'])

  serverProcess.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`)
  })

  serverProcess.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`)
  })

  // Encerrar o servidor Flask quando a janela do Electron for fechada
  mainWindow.on('closed', () => {
    serverProcess.kill()
  })
}

app.whenReady().then(createWindow)