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

    def test_thing(self):
        response = self.app.get('/')
        assert response.status_code == 200