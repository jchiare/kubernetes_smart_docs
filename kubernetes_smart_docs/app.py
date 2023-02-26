from flask import Flask
from kubernetes_smart_docs.api import reply
from kubernetes_smart_docs import home

def create_app():
    app = Flask(__name__)
    
    app.secret_key = 'secret_key' # ... change this
    app.register_blueprint(reply.reply_blueprint)
    app.register_blueprint(home.bp)

    return app  
