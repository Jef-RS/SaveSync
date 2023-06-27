from flask import Flask, render_template, request, redirect, url_for
from Backend.game_config import packet_base, packet_bd
import os , json


diretório = os.path.dirname(__file__)
name_arq = os.path.basename(diretório)
diretório_raiz= diretório[:-len('Backend/routes')]

dir_absp = diretório_raiz
dir_frontend_templates = f'{dir_absp}/Frontend/templates'
dir_frontend_static = f'{dir_absp}/Frontend/static'

usuarios =[]

app = Flask(__name__, template_folder=dir_frontend_templates, static_folder=dir_frontend_static)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/chamar_funcao', methods=['POST'])
def chamar_funcao():

    try:
        jogo1 = str(request.form['jogo1'])
        jogo2 = str(request.form['jogo2'])
        packet_base.adicionar_games_bd(jogo1, jogo2)

    except BaseException as e:
        print(f'Quase lá {e}')

    return "SUCESSO" + json.dumps(packet_bd.read_games())


@app.route('/login', methods=['GET', 'POST'])
def login():
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
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)