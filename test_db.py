from flask import Flask
from flaskblog import routes, app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request, abort
import os
import tempfile
import pytest
from unittest import TestCase
from flaskblog.models import User
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename



def _init_database():
    hashed_password = bcrypt.generate_password_hash('killmeplz').decode('utf-8')
    user = User(username="john", email="john@example.com", password=hashed_password)
    db.session.add(user)
    db.session.commit()

class ModelsTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        db.drop_all()
        db.create_all()
        _init_database() 

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_case_1(self):
        self.assertTrue(User.query.count() == 1)

if __name__ == '__main__':
    unittest.main()