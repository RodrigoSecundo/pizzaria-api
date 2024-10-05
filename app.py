from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de Cliente
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)  # Adiciona a coluna de senha

# Cria o banco de dados se não existir
with app.app_context():
    db.create_all()

# Rota da página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']  # Obtém a senha do formulário
        novo_cliente = Cliente(nome=nome, email=email, senha=senha)
        db.session.add(novo_cliente)
        db.session.commit()  # Salva no banco de dados
        return redirect(url_for('visualizar'))  # Redireciona para a página de visualização
    return render_template('register.html')

# Rota de visualização
@app.route('/visualizar')
def visualizar():
    clientes = Cliente.query.all()  # Busca todos os clientes no banco de dados
    return render_template('visualizar.html', clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)
