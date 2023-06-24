from flask import Flask, render_template
import os

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

@app.route('/login')
def page2():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)