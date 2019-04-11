from flask import Flask
from flaskblog import routes, app
from flask import render_template, url_for, flash, redirect, request, abort
import os
import tempfile
import pytest
from unittest import TestCase

class TestIntegrations(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        assert response.status_code == 200
        response = self.app.get('/home')
        assert response.status_code == 200

    def test_about(self):
        response = self.app.get('/about')
        assert response.status_code == 200

    def test_register(self):
        response = self.app.get('/register')
        assert response.status_code == 200

    def test_login(self):
        response = self.app.get('/login')
        assert response.status_code == 200

    def test_results(self):
        response = self.app.get('/results')
        assert response.status_code == 200

    if __name__ == "__main__":
        unittest.main()
        