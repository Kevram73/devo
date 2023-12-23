from flask import Flask, request, jsonify
from service.models import Entity
from service import db


class EntityController:
    def __init__(self):
        pass
    
    @staticmethod
    def get_entities():
        entities = Entity.query.all()
        return jsonify([str(entity) for entity in entities])

    @staticmethod
    def get_entity(entity_id):
        entity = Entity.query.get(entity_id)
        if entity:
            return jsonify(str(entity))
        return jsonify({"error": "Entity not found"}), 404

    @staticmethod
    def create_entity():
        data = request.get_json()
        new_entity = Entity(**data)
        db.session.add(new_entity)
        db.session.commit()
        return jsonify(str(new_entity)), 201

    @staticmethod
    def update_entity(entity_id):
        entity = Entity.query.get(entity_id)
        if entity:
            data = request.get_json()
            entity.nom = data.get('nom', entity.nom)
            entity.adresse = data.get('adresse', entity.adresse)
            entity.tel = data.get('tel', entity.tel)
            db.session.commit()
            return jsonify(str(entity))
        return jsonify({"error": "Entity not found"}), 404

    @staticmethod
    def delete_entity(entity_id):
        entity = Entity.query.get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return jsonify({"message": "Entity deleted successfully"})
        return jsonify({"error": "Entity not found"}), 404

# Routes