from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "your_secret_key"

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''   # your MySQL password
app.config['MYSQL_DB'] = 'pm_crud'

mysql = MySQL(app)

# Home Page - Show Records
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', users=data)

# Add User
@app.route('/add', methods=['POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        flash("User Added Successfully")
        return redirect(url_for('index'))

# Edit User
@app.route('/edit/<id>', methods=['POST', 'GET'])
def edit_user(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id=%s", (id,))
    data = cur.fetchone()
    cur.close()
    return render_template('edit.html', user=data)

# Update User
@app.route('/update/<id>', methods=['POST'])
def update_user(id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE users
            SET name=%s, email=%s, phone=%s
            WHERE id=%s
        """, (name, email, phone, id))
        mysql.connection.commit()
        flash("User Updated Successfully")
        return redirect(url_for('index'))

# Delete User
@app.route('/delete/<id>', methods=['GET'])
def delete_user(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (id,))
    mysql.connection.commit()
    flash("User Deleted Successfully")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
