# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 10:22:47 2025

@author: enzo
"""

from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # clé primaire unique
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
