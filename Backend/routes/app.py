from flask import Flask, render_template, request, redirect, url_for
from gamebd_config import packetG_base, packetG_bd
from userbd_config import packetU_base, packetU_bd
from time import sleep
import os




diretório = os.path.dirname(__file__)
name_arq = os.path.basename(diretório)
diretório_raiz = diretório[: -len('Backend/routes')]


dir_absp = diretório_raiz
dir_frontend_templates = f'{dir_absp}/Backend/routes/templates'
dir_frontend_static = f'{dir_absp}/Backend/routes/static/'

usuarios = []

image_list = ['profile__test.jpg']

app = Flask(
    __name__
)
read_users = packetU_bd.read_users()

@app.route('/')
def start():
    """
    Decorador do Flask para a rota '/'. Renderiza o template 'index.html'.

    Parâmetros:
        Nenhum.

    Retorna:
        O template renderizado 'index.html'.
    """
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    
    image = request.files['image']
    image.save(f'{dir_frontend_static}/images/profile_image/' + image.filename)
    image_list.append(image.filename)
    
    return redirect(url_for('page3'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Rota para lidar com o login do usuário. Aceita solicitações GET e POST.
    Se uma solicitação POST for feita, verifica o nome de usuário e a senha
    fornecidos em relação a uma lista pré-definida de usuários. Se uma
    correspondência for encontrada, o usuário é redirecionado para a página inicial.
    Caso contrário, uma mensagem de erro é exibida. Retorna um modelo renderizado
    para a página de login com a mensagem de erro (se houver).
    """
    
    mensagem = ' Seja bem-vindo.'
    read_users = packetU_bd.read_users()
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        usuarios.append(username)
        for dicionario in read_users:
            usernamedict = dicionario['username']
            passworddict = dicionario['password']
            if username == usernamedict and password == passworddict:           
                return redirect('home')
        error = 'Usuário ou senha inválidos.'
    return render_template('login.html', error=error, mensagem=mensagem)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    """
    Registra um novo usuário, adicionando seu nome de usuário e senha à lista `usuarios` se as senhas coincidirem
    e se o nome de usuário ainda não estiver sendo utilizado.

    Argumentos:
    Nenhum.

    Retornos:
        Dependendo do método de solicitação:
        GET: Retorna o modelo 'cadastro.html' renderizado.
        POST:
            * Se as senhas não coincidirem: Retorna a mesma página 'cadastro.html' com uma mensagem de erro.
            * Se o nome de usuário já estiver sendo utilizado: Retorna a mesma página 'cadastro.html' com uma mensagem de erro.
            * Se o usuário for registrado com sucesso: Redireciona para a página 'login'.
    """
    read_users = packetU_bd.read_users()
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirma_password = request.form['confirma_password']
        
        if password != confirma_password:
            error = 'As senhas não coincidem.'

        for dict in read_users:
            if username == dict['username']:
                error = 'Usuário já cadastrado.'
                    
        if error is None:
            packetU_base.adicionar_users_bd(username, password) 
            print('SEM ERRO !')
            return redirect(url_for('login'))
    return render_template('cadastro.html', error = error)

    
@app.route('/home')
def page3():
    """
    Decorador que mapeia a URL '/home' para a função 'page3()'.
    Renderiza o template 'home.html' e retorna o resultado como um objeto de resposta.
    """
    for image in image_list:
        image_file = image
    for user in usuarios:
        user_name = user
    return render_template('home.html', user_name=user_name, imagefile=image_file) 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


