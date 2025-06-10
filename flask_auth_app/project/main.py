# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 09:47:56 2025

@author: enzo
"""
from flask import Blueprint, render_template

from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')