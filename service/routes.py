from service import app, login_manager
from flask import jsonify, request
from service.controllers.authController import AuthController
from flask_login import LoginManager, login_required
from service.controllers.entityController import EntityController
from service.controllers.categoriePlatController import CategoriePlatController
from service.controllers.homeController import HomeController
from service.controllers.platController import PlatController

from service.models import User

authController = AuthController()
homeController = HomeController()
entityController = EntityController()
categoriePlatController = CategoriePlatController()
platController = platController()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



app.add_url_rule('/', view_func=authController.login, methods=['POST'])
app.add_url_rule('/', view_func=authController.login_page, methods=['GET'])
app.add_url_rule('/register', view_func=authController.register_user, methods=['POST'])
app.add_url_rule('/logout', view_func=authController.logout, methods=['POST'])

app.add_url_rule('/dashboard', view_func=homeController.index, methods=['GET'])

app.add_url_rule('/entities', view_func=entityController.get_entities, methods=['GET'])
app.add_url_rule('/entities/<int:entity_id>', view_func=entityController.get_entity, methods=['GET'])
app.add_url_rule('/entities', view_func=entityController.create_entity, methods=['POST'])
app.add_url_rule('/entities/<int:entity_id>', view_func=entityController.update_entity, methods=['PUT'])
app.add_url_rule('/entities/<int:entity_id>', view_func=entityController.delete_entity, methods=['DELETE'])

app.add_url_rule('/categories', view_func=categoriePlatController.get_categories, methods=['GET'])
app.add_url_rule('/categories/<int:category_id>', view_func=categoriePlatController.get_category, methods=['GET'])
app.add_url_rule('/categories', view_func=categoriePlatController.create_category, methods=['POST'])
app.add_url_rule('/categories/<int:category_id>', view_func=categoriePlatController.update_category, methods=['PUT'])
app.add_url_rule('/categories/<int:category_id>', view_func=categoriePlatController.delete_category, methods=['DELETE'])

app.add_url_rule('/plats', view_func=platController.get_plats, methods=['GET'])
app.add_url_rule('/plats/<int:plat_id>', view_func=platController.get_plat, methods=['GET'])
app.add_url_rule('/plats', view_func=platController.create_plat, methods=['POST'])
app.add_url_rule('/plats/<int:plat_id>', view_func=platController.update_plat, methods=['PUT'])
app.add_url_rule('/plats/<int:plat_id>', view_func=platController.delete_plat, methods=['DELETE'])
