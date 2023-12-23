from flask import jsonify
from service import db
import datetime
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin

# Resto | Bar
class Entity(db.Model, SerializerMixin): 
    __tablename__ = 'entities'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255))
    adresse = db.Column(db.String(255))
    tel = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    
    def __str__(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "tel": self.tel,
            "adresse": self.adresse,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        
        
class CategoriePlat(db.Model, SerializerMixin): 
    __tablename__ = 'categorie_plats'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255))
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    

class Plat(db.Model, SerializerMixin): 
    __tablename__ = 'plats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    price = db.Column(db.Float())
    status = db.Column(db.Boolean())
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    
class Role(db.Model, SerializerMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())

class User(db.Model, UserMixin, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    
    def role(self):
        return Role.query.filter_by(id=self.role_id).first()

class Table(db.Model):
    __tablename__ = "tables"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(255))
    capacity = db.Column(db.Integer)
    status = db.Column(db.Integer)
    entity = db.Column(db.Integer, db.ForeignKey('roles.id'))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())



class Command(db.Model):
    __tablename__ = "commands"
    id = db.Column(db.Integer, primary_key=True)
    date_command = db.Column(db.DateTime(timezone=True))
    table = db.Column(db.Integer, db.ForeignKey('tables.id'))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())


class LineCommand(db.Model):
    __tablename__ = "line_commands"
    id = db.Column(db.Integer, primary_key=True)
    plat = db.Column(db.Integer, db.ForeignKey('plats.id'))
    command = db.Column(db.Integer, db.ForeignKey('commands.id'))
    quantity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    
class CategorieProduit(db.Model):
    __tablename__ = "categorie_produits"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True))
    libelle = db.Column(db.String(255))
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    
    def __str__(self):
        return str(self.libelle)
        


class FamilleProduit(db.Model):
    __tablename__ = "famille_produits"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True))
    libelle = db.Column(db.String(255))
    description = db.Column(db.String(255))
    categorie = db.Column(db.Integer, db.ForeignKey('categorie_produits.id'))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    
    def __str__(self):
        return str(self.libelle)



class Produit(db.Model):
    __tablename__ = "produits"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True))
    libelle = db.Column(db.String(255))
    description = db.Column(db.String(255))
    prix_unitaire = db.Column(db.Float())
    unite = db.Column(db.Integer())
    famille = db.Column(db.Integer, db.ForeignKey('famille_produits.id'))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    
    def __str__(self):
        return str(self.libelle)
    

class StockEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True))
    produit = db.Column(db.Integer, db.ForeignKey('produits.id'))
    valeur = db.Column(db.Float())
    quantite =db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    
    def __str__(self):
        return str(self.produit)


class StockOutResto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True))
    produit = db.Column(db.Integer, db.ForeignKey('produits.id'))
    valeur = db.Column(db.Float())
    quantite =db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    