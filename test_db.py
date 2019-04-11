from flask import Flask
from flaskblog import routes, app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request, abort
import os
import tempfile
import pytest
from unittest import TestCase
from flaskblog.models import User, Post
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename



def add_user():
    hashed_password = bcrypt.generate_password_hash('killmeplz').decode('utf-8')
    user = User(username="John", email="john@example.com", password=hashed_password)
    db.session.add(user)
    db.session.commit()

class ModelsTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        db.drop_all()
        db.create_all()
        add_user() 

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user(self):
        self.assertTrue(User.query.count() == 1)
        hashed_password = bcrypt.generate_password_hash('killmepls').decode('utf-8')
        user = User(username="Lizzy", email="liz@example.com", password=hashed_password)
        db.session.add(user)
        db.session.commit()
        self.assertTrue(User.query.count() == 2)
        user1 = User.query.first()
        assert user1.username == "John"

    def test_post(self):
        user = User(username="Lizzy", email="liz@example.com", password="password")
        post = Post(title="Death", alg_file = "death.py", content="description", author=user)
        db.session.add(post)
        db.session.commit()
        self.assertTrue(Post.query.count() == 1)
        post1 = Post.query.first()
        assert post1.title == "Death"
        assert post1.alg_file == "death.py"

    if __name__ == '__main__':
        unittest.main()