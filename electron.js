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
      nodeIntegration: true,
      contextIsolation: false,
    },
  });

  const filePath = store.get('filePath');

  if (filePath) {
    mainWindow.loadURL(`file://${path.join(__dirname, '../build/index.html')}?path=${encodeURIComponent(filePath)}`);
  } else {
    mainWindow.loadURL(`file://${path.join(__dirname, '../build/index.html')}`);
  }

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

ipcMain.on('select-directory', (event) => {
  const { dialog } = require('electron');
  dialog
    .showOpenDialog(mainWindow, {
      properties: ['openDirectory'],
    })
    .then((result) => {
      if (!result.canceled && result.filePaths.length > 0) {
        store.set('filePath', result.filePaths[0]);
        event.sender.send('selected-directory', result.filePaths[0]);
      }
    })
    .catch((err) => {
      console.log(err);
    });
});

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});
