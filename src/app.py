from flask import Flask, redirect, render_template, request, url_for, flash, session
from config import config

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  

USUARIOS_VALIDOS = {
    'admin': '123',
    'usuario1': 'clave123',
    'usuario2': 'segura456'
}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
           
        if username in USUARIOS_VALIDOS and USUARIOS_VALIDOS[username] == password:
            session['usuario'] = username  
            flash('¡Has iniciado sesión correctamente!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
    
    return render_template('auth/login.html')

@app.route('/home')
def home():
    if 'usuario' not in session:
        flash('Por favor inicia sesión primero', 'warning')
        return redirect(url_for('login'))
    
    return render_template('home.html', usuario=session['usuario'])

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Has cerrado sesión correctamente', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()

    #jose trejo 20491190