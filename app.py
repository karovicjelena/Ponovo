from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
CORS(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Directly create tables without using a decorator
with app.app_context():
    db.create_all()

# Routes
@app.route('/api/signup', methods=['POST'])
def signup():
    # Your signup route logic...
    pass

@app.route('/api/login', methods=['POST'])
def login():
    # Your login route logic...
    pass

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
