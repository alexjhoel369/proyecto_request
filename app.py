from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inscripcion_curso', methods=['GET', 'POST'])
def inscripcion_curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        curso = request.form['curso']
        return f"Inscripción recibida: {nombre} {apellido}, Curso: {curso}"
    return render_template('curso.html')

@app.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        return f"Usuario registrado: {nombre} {apellido}, Correo: {correo}"
    return render_template('usuario.html')

@app.route('/registro_producto', methods=['GET', 'POST'])
def registro_producto():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        return f"Producto registrado: {producto}, Categoría: {categoria}, Existencia: {existencia}, Precio: {precio}"
    return render_template('producto.html')

@app.route('/registro_libro', methods=['GET', 'POST'])
def registro_libro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form['medio']
        return f"Libro registrado: {titulo} por {autor}, Medio: {medio}"
    return render_template('libro.html')

if __name__ == '__main__':
    app.run(debug=True)
