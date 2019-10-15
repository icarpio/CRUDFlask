from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL



app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'agenda'

mysql = MySQL(app)



@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM contactos")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', contactos=data )



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Datos insertados correctamente")
        name = request.form['nombre']
        email = request.form['email']
        phone = request.form['telefono']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contactos (nombre, email, telefono) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/update', methods = ['POST','GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['nombre']
        email = request.form['email']
        phone = request.form['telefono']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE contactos SET nombre=%s, email=%s, telefono=%s WHERE id=%s", (name,email,phone,id_data))
        flash("Datos actualizados correctamente")
        mysql.connection.commit()
        return redirect(url_for('Index'))



if __name__ == "__main__":
    app.run(debug=True)
