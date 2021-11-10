from application import app
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL, MySQLdb

app.secret_key ="secretkeyular"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_fp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('home.html')


# mengirimkan data atau nilai langsung ke action untuk ditampung, tanpa menampilkan pada URL
@app.route('/contactInput', methods=['POST'])
def contactInput():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        cur.execute("INSERT INTO contact (nama, email, subject, message) VALUES (%s,%s,%s,%s)", (nama, email, subject, message))
        mysql.connection.commit()
        flash('Pesan Telah Terkirim')
        return render_template("home.html", index=False)