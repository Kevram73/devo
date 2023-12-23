from functools import wraps
from flask import flash, redirect, render_template, request, session, jsonify, url_for
import flask_bcrypt
from service.models import User
from service import db, app
from flask_login import LoginManager, login_user, logout_user


class AuthController:
    def __init__(self):
        pass
    
    @staticmethod
    def login(self, data):
        user = User.query.filter_by(email=data['email']).first()
        if user and flask_bcrypt.check_password_hash(user.password, data['password']):
            login_user(user)
            flash('Connexion réussie!', 'success')  # Flash success message
            return redirect(url_for('dashboard'))  # Adjust 'dashboard' to your actual dashboard route
        else:
            return flash('Email ou mot de passe invalide', 'error')  # Flash error message
    @staticmethod
    def login_page(self):
        return render_template('pages/auth/login.html')       

    @staticmethod
    def register_user(self, data):
        data = request.get_json()
        newUser = User(
                    username=data['username'], 
                    email=data['email'], 
                    password=flask_bcrypt.generate_password_hash(data['password']), 
                    role_id=data['role_id']
                )
        db.session.add(newUser)
        db.session.commit()
        return jsonify({"data": newUser.to_dict(), 'success': True})

    @staticmethod
    def logout():
        logout_user()
        flash('Vous avez été déconnecté avec succès.', 'info')
        return redirect(url_for('login'))