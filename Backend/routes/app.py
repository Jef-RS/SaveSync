from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, render_template, request, redirect, url_for
from data import bd
import os

usuarios = []

#Cria a conexão com o banco de dados
Session = sessionmaker(bind=bd.engine)

#Cria a instância do Base
Base = declarative_base()

#Define a classe do modelo
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name_user = Column(String)
    password_user = Column(String)

#Cria o banco de dados
Base.metadata.create_all(bd.engine)

#Cria uma nova instância do User
user = User(name_user=usuarios['username'], password_user=usuarios['password'])

def save():
    session = Session()
    try:
        #Adiciona o usuario à sessão
        session.add(user)

        #Salva as mudanças no banco de dados
        session.commit()

        print("Usuario criado e salvo com sucesso!")
    except Exception as e:
        #Em caso de erro, faz rollback na transação
        session.rollback()
        print("Erro ao criar e salvar o usuario:", str(e))
    finally:
        #Fecha a sessão
        session.close() 

diretório = os.path.dirname(__file__)
name_arq = os.path.basename(diretório)
diretório_raiz= diretório[:-len('Backend/routes')]

dir_absp = diretório_raiz
dir_frontend_templates = f'{dir_absp}/Frontend/templates'
dir_frontend_static = f'{dir_absp}/Frontend/static'

app = Flask(__name__, template_folder=dir_frontend_templates, static_folder=dir_frontend_static)

@app.route('/')
def start():
    return render_template('index.html')


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