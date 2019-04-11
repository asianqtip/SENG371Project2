import pytest
import unittest
import requests

    def test_get_games():
        res = requests.get('http://localhost:5000/')
        self.assertEqual(res.status_code, 200)
