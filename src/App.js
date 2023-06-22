import React from 'react';
import { ipcRenderer } from 'electron';

function App() {
  const handleOpenDirectory = () => {
    ipcRenderer.send('select-directory');
  };

  return (
    <div className="App">
      <button onClick={handleOpenDirectory}>Abrir Diretório</button>
    </div>
  );
}

export default App;
