from flask import Flask, render_template

# definir como archivo de arranque
app = Flask(__name__)

# crear una ruta de la pagina principal


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)  # ejecutar aplicacion en modo de prueba
