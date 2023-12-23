from flask import render_template
from flask_login import current_user

class HomeController:
    def __init__(self) -> None:
        pass
    
    def index(self):
        return render_template("pages/main/index.html", user=current_user)