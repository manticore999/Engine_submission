
from flask import Flask
from routes.api import api_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    
    app.run(debug=True, host='0.0.0.0', port=3033)
