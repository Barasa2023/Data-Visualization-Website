from flask import Flask
from routes import data, visualizations, auth, admin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize the database
db = SQLAlchemy(app)

# Register Blueprints
app.register_blueprint(data.bp)
app.register_blueprint(visualizations.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(admin.bp)

if __name__ == '__main__':
    app.run(debug=True)