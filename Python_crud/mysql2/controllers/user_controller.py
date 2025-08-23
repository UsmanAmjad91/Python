from flask import render_template, request, redirect, url_for, flash
from models.user_model import UserModel

class UserController:
    @staticmethod
    def index():
        users = UserModel.get_all()
        return render_template("index.html", users=users)
    
    @staticmethod
    def add():
        return render_template("add.html")
    
    @staticmethod
    def create():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            UserModel.insert(name, email, phone)
            flash("User Added Successfully")
            return redirect(url_for('index'))

    @staticmethod
    def edit(user_id):
        user = UserModel.get_by_id(user_id)
        return render_template("edit.html", user=user)

    @staticmethod
    def update(user_id):
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            UserModel.update(user_id, name, email, phone)
            flash("User Updated Successfully")
            return redirect(url_for('index'))

    @staticmethod
    def delete(user_id):
        UserModel.delete(user_id)
        flash("User Deleted Successfully")
        return redirect(url_for('index'))
