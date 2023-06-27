from flask import Flask, render_template, request, redirect, url_for

# from Backend.game_config import packet_base, packet_bd
import os, json


diretório = os.path.dirname(__file__)
name_arq = os.path.basename(diretório)
diretório_raiz = diretório[: -len('Backend/routes')]

dir_absp = diretório_raiz
dir_frontend_templates = f'{dir_absp}/Frontend/templates'
dir_frontend_static = f'{dir_absp}/Frontend/static'

usuarios = []

app = Flask(
    __name__,
    template_folder=dir_frontend_templates,
    static_folder=dir_frontend_static,
)


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


@app.route('/test')
def test():
    """
    Esta função é um decorador de rota para o endpoint '/test' que aceita requisições GET.
    Quando chamada, ela renderiza o modelo 'test.html' e retorna o resultado como um objeto de resposta.
    Retorna:
        Um modelo HTML renderizado como um objeto de resposta.
    """
    return render_template('test.html')


@app.route('/chamar_funcao', methods=['POST'])
def chamar_funcao():
    """
    Esta função é um endpoint da aplicação Flask que adiciona dois jogos a um banco de dados através de uma
    requisição POST. Os jogos são obtidos dos campos 'jogo1' e 'jogo2' do formulário da requisição. A função
    retorna um JSON contendo todos os jogos no banco de dados. Se uma exceção for lançada, a função exibe uma
    mensagem de erro e retorna None.

    :return: Um JSON contendo todos os jogos no banco de dados.
    """

    try:
        jogo1 = str(request.form['jogo1'])
        jogo2 = str(request.form['jogo2'])
        packet_base.adicionar_games_bd(jogo1, jogo2)

    except BaseException as e:
        print(f'Quase lá {e}')

    return 'SUCESSO' + json.dumps(packet_bd.read_games())


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

    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in usuarios:
            if user['username'] == username and user['password'] == password:
                return redirect('home')
        error = 'Usuário ou senha inválidos.'
    return render_template('login.html', error=error)


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

    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirma_password = request.form['confirma_password']
        if password != confirma_password:
            error = 'As senhas não coincidem.'
        else:
            for user in usuarios:
                if user['username'] == username:
                    error = 'Usuário já cadastrado.'
            if error is None:
                usuarios.append({'username': username, 'password': password})
                return redirect(url_for('login'))
    return render_template('cadastro.html')


@app.route('/home')
def page3():
    """
    Decorador que mapeia a URL '/home' para a função 'page3()'.
    Renderiza o template 'home.html' e retorna o resultado como um objeto de resposta.
    """

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
