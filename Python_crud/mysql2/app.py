from flask import Flask
from config.db import init_app
from controllers.user_controller import UserController

app = Flask(__name__)
app.secret_key = "secret123"

# Initialize MySQL
init_app(app)

# Routes
app.add_url_rule('/', view_func=UserController.index)
app.add_url_rule('/add/user', view_func=UserController.add, methods=['GET'])
app.add_url_rule('/create', view_func=UserController.create, methods=['POST'])
app.add_url_rule('/edit/<int:user_id>', view_func=UserController.edit, methods=['GET'])
app.add_url_rule('/update/<int:user_id>', view_func=UserController.update, methods=['POST'])
app.add_url_rule('/delete/<int:user_id>', view_func=UserController.delete, methods=['GET'])

if __name__ == "__main__":
    app.run(debug=True)
