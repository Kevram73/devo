from flask import Flask, request, jsonify
from service.models import CategoriePlat
from service import db

class CategoriePlatController:
    def __init__(self):
        pass
    
    @staticmethod
    def get_categories():
        categories = CategoriePlat.query.all()
        return jsonify([str(category) for category in categories])

    @staticmethod
    def get_category(category_id):
        category = CategoriePlat.query.get(category_id)
        if category:
            return jsonify(str(category))
        return jsonify({"error": "Category not found"}), 404

    @staticmethod
    def create_category():
        data = request.get_json()
        new_category = CategoriePlat(**data)
        db.session.add(new_category)
        db.session.commit()
        return jsonify(str(new_category)), 201

    @staticmethod
    def update_category(category_id):
        category = CategoriePlat.query.get(category_id)
        if category:
            data = request.get_json()
            category.nom = data.get('nom', category.nom)
            category.description = data.get('description', category.description)
            db.session.commit()
            return jsonify(str(category))
        return jsonify({"error": "Category not found"}), 404

    @staticmethod
    def delete_category(category_id):
        category = CategoriePlat.query.get(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()
            return jsonify({"message": "Category deleted successfully"})
        return jsonify({"error": "Category not found"}), 404


