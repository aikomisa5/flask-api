from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from datetime import timedelta

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

#app.config['JWT_AUTH_URL_RULE'] = '/login'
#app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
#app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/stores/<string:name>')
api.add_resource(Item, '/items/<string:name>') #http://localhost:5000/items/sarasa
api.add_resource(ItemList, '/items') #http://localhost:5000/items
api.add_resource(StoreList, '/stores') #http://localhost:5000/items
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)

