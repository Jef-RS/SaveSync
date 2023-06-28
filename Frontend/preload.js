
function installRequirements() /**
* Instala os pacotes necessários especificados no arquivo requirements.txt.
*
* @param {type} - Nenhum parâmetro necessário.
* @return {type} - Sem valor de retorno.
*/
{
  exec('pip install -r requirements.txt', (error, stdout, stderr) => {
    if (error) {
      console.error(`Erro ao instalar os pacotes: ${error}`);
      return;
    }
    console.log(`Pacotes instalados com sucesso: ${stdout}`);
  });
}

// Chamada da função para instalar os pacotes
installRequirements();