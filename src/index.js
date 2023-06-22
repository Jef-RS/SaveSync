import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { ipcRenderer } from 'electron';

ipcRenderer.on('selected-directory', (event, path) => {
  console.log('Selected Directory:', path);
});

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
