from flaskblog import app
from os import environ

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=environ.get("PORT", 5000))
