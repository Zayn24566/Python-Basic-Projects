from flask import Flask
from models import db
from config import Config
from routes import register_routes
from flask_cors import CORS
 
app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
 
db.init_app(app)
 
with app.app_context():
    db.create_all()
 
register_routes(app)
 
if __name__ == '__main__':
    app.run(debug=True)
 