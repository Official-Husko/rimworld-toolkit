from flask import Flask
import random, string
import os, random

def create_app():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(255))
    #app.config['TESTING'] = True
    #app.config["env"] = "production"
    
    from .views import views

    app.register_blueprint(views, url_prefix="/")
    
    return app