from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL connection configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Zinedine2015!',
    'database': 'db_registra'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    birth_date = request.form['birth_date']
    email = request.form['email']

    # Connect to MySQL and insert data
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "INSERT INTO tbl_student (first_name, last_name, birth_date, email) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (first_name, last_name, birth_date, email))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
