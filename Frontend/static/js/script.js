function exibirPopup() {
    // Cria um elemento de div para o pop-up
    var popup = document.createElement('div');
    popup.className = 'popup';
    
    // Cria um elemento de parágrafo para exibir a mensagem
    var mensagem = document.createElement('p');
    mensagem.textContent = 'Usuário cadastrado com sucesso!';
    
    // Adiciona a mensagem ao pop-up
    popup.appendChild(mensagem);
    
    // Adiciona o pop-up ao corpo do documento
    document.body.appendChild(popup);
    
    // Remove o pop-up após 3 segundos
    setTimeout(function() {
      document.body.removeChild(popup);
    }, 3000);
  }
  
  
  
  exibirPopup();
  