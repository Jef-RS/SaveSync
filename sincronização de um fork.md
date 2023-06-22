## Como enviar um push para o diretório de alguém que eu fiz o fork

Se você fez um fork de um repositório e deseja enviar suas alterações para o diretório do proprietário original, você precisará seguir algumas etapas adicionais.

1. Configure o repositório remoto do diretório do proprietário original:
   No seu ambiente local, adicione o repositório original como um repositório remoto. Para fazer isso, execute o seguinte comando em seu terminal, substituindo `<URL_DO_REPOSITORIO>` pela URL do repositório original:

~~~bash
git remote add upstream https://github.com/eusouanderson/SaveSync.git
~~~

2. Atualize o repositório local:
Para garantir que você esteja trabalhando com a versão mais recente do repositório original, execute o seguinte comando em seu terminal:

~~~bash
git fetch upstream
~~~


3. Mescle as alterações do repositório original ao seu ramo:
Com as alterações do repositório original atualizadas em seu repositório local, você pode mesclar essas alterações ao seu ramo. Certifique-se de estar no seu ramo principal (por exemplo, "main" ou "master") e execute o seguinte comando:

~~~bash
git branch 
~~~

para verificar qual seu ramo atual

~~~bash
git merge upstream/main
~~~

Isso mesclará as alterações do repositório original ao seu ramo.

4. Resolva quaisquer conflitos:
Se houver conflitos durante a mesclagem, você precisará resolvê-los manualmente. O Git indicará os arquivos com conflitos e você precisará editar esses arquivos para resolver as diferenças. Após resolver os conflitos, faça um commit das alterações resultantes.

5. Envie as alterações para o seu fork:
Após mesclar as alterações do repositório original ao seu ramo, você pode enviar essas alterações para o seu fork. Use o seguinte comando para enviar as alterações:

~~~bash
git push origin main
~~~


Substitua "main" pelo nome do seu ramo principal, se necessário.

6. Envie um pull request ao repositório original:
Após enviar as alterações para o seu fork, você pode seguir as etapas mencionadas anteriormente para enviar um pull request ao repositório original. Isso permitirá que o proprietário original revise suas alterações e as incorpore ao repositório original, se apropriado.

É importante lembrar que você não pode enviar um push diretamente para o repositório original, pois você fez um fork dele. Em vez disso, você envia as alterações para o seu fork e, em seguida, solicita que o proprietário original as incorpore por meio de um pull request.
