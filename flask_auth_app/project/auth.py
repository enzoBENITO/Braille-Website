# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 09:50:01 2025

@author: enzo
"""

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])  # POST : traite les données
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return redirect(url_for('auth.login'))

    return "Connexion réussie !"

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # Vérifie si l'utilisateur existe déjà
    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')

        return redirect(url_for('auth.signup'))

    # Hash du mot de passe (important pour la sécurité !)
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    # Création de l'utilisateur
    new_user = User(
    email=email,
    name=name,
    password=hashed_password  
)


    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return "Logout"

