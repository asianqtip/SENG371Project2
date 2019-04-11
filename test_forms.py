from flask import Flask
from flaskblog import routes, app
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, UploadForm
from flask import render_template, url_for, flash, redirect, request, abort
import os
import tempfile
import pytest
from unittest import TestCase


class FormTest(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_login(self):
        with app.test_request_context('/login'):
            form = LoginForm()
        self.assertIsInstance(form, LoginForm)

    def test_register(self):
        with app.test_request_context('/register'):
            form = RegistrationForm()
        self.assertIsInstance(form, RegistrationForm)
    
    def test_upload(self):
        with app.test_request_context('/upload'):
            form = UploadForm()
        self.assertIsInstance(form, UploadForm)
    
    if __name__ == "__main__":
        unittest.main()

    