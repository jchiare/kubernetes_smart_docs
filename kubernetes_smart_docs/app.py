from flask import Flask
from kubernetes_smart_docs.api import reply

def create_app():
    app = Flask(__name__)
    
    app.secret_key = 'secret_key' # ... change this
    app.register_blueprint(reply.reply_blueprint)

    return app  
