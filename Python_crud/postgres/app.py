from flask import Flask, render_template, request, redirect, url_for
from models import db, User
from config import Config



app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

# Home page - list users
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

# Add user
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        user = User(name=name, email=email, age=age)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html')

# Edit user
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get(id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        user.age = request.form['age']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_user.html', user=user)

# Delete user
@app.route('/delete/<int:id>')
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
