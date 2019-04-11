from flask import request
from flaskblog import routes

def test_home():
    app=Flask(__name__)
    client = app.test_client()
    url='l'
    response = client.get(url)
    assert response.status_code == 200