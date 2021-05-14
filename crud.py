from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_enum import EnumField
from marshmallow import fields, validate, exceptions
from country import Country
from colour import Colour
from material import Material
from utility import Utility
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'.format(
    user=str(os.getenv('user')),
    password=str(os.getenv('password')),
    host=str(os.getenv('host')),
    port=str(os.getenv('port')),
    database=str(os.getenv('database'))
)
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Basket(db.Model):
    __tablename__ = 'baskets'
    id = db.Column(db.Integer, primary_key=True)
    basketname = db.Column(db.String(80), unique=True)
    country_of_origin = db.Column(db.Enum(Country))
    colour = db.Column(db.Enum(Colour))
    material = db.Column(db.Enum(Material))
    number_of_handles = db.Column(db.Integer)
    price_in_uah = db.Column(db.Float)
    size_in_liters = db.Column(db.Float)
    utility = db.Column(db.Enum(Utility))
    weight_in_grams = db.Column(db.Float)
    
    def __init__(self, basketname= "N/A", country_of_origin=Country.RUSSIA, colour=Colour.TRANSPARENT, 
                 material=Material.WOOD, number_of_handles=0, price_in_uah=0.0, size_in_liters=0.0, 
                 utility=Utility.DECORATIVE, weight_in_grams=0.0):
                 self.basketname = basketname
                 self.country_of_origin = country_of_origin
                 self.colour = colour
                 self.material = material
                 self.number_of_handles = number_of_handles
                 self.price_in_uah = price_in_uah
                 self.size_in_liters = size_in_liters
                 self.utility = utility
                 self.weight_in_grams = weight_in_grams
    def update(self, basketname, country_of_origin, colour, 
                 material, number_of_handles, price_in_uah, size_in_liters, 
                 utility, weight_in_grams):
                 self.__init__(basketname, country_of_origin, colour, material, number_of_handles, price_in_uah,
                               size_in_liters, utility, weight_in_grams)
                               

def get_basket_by_id(id):
    basket = Basket.query.get(id)
    if basket is None:
        return abort(404)
    return basket

class BasketSchema(ma.Schema):
    country_of_origin = EnumField(Country)
    colour = EnumField(Colour)
    material = EnumField(Material)
    utility = EnumField(Utility)
    basketname = fields.String(validate=validate.Length(max=80))

    class Meta:
        # Fields to expose
        fields = ('basketname', 'country_of_origin', 'colour', 'material', 'number_of_handles', 
        'price_in_uah', 'size_in_liters', 'utility', 'weight_in_grams')


basket_schema = BasketSchema()
baskets_schema = BasketSchema(many=True)

@app.errorhandler(exceptions.ValidationError)
def handle_exception(e):
    return e.messages, 400

# endpoint to create new basket
@app.route("/basket", methods=["POST"])
def add_basket():
    fields = basket_schema.load(request.json)
    new_basket = Basket(**fields)

    db.session.add(new_basket)
    db.session.commit()

    return basket_schema.jsonify(new_basket)


# endpoint to show all baskets
@app.route("/basket", methods=["GET"])
def get_basket():
    all_baskets = Basket.query.all()
    result = baskets_schema.dump(all_baskets)
    return jsonify(result)


# endpoint to get basket detail by id
@app.route("/basket/<id>", methods=["GET"])
def basket_detail(id):
    basket = get_basket_by_id(id)
    return basket_schema.jsonify(basket)

# endpoint to get a teapot state code
@app.route("/teapot", methods=["GET"])
def teapot_detail():
    abort(418)
    return None

# endpoint to update basket 
@app.route("/basket/<id>", methods=["PUT"])
def basket_update(id):
    basket = get_basket_by_id(id)
    fields = basket_schema.load(request.json)

    basket.update(**fields)

    db.session.commit()
    return basket_schema.jsonify(basket)


# endpoint to delete basket
@app.route("/basket/<id>", methods=["DELETE"])
def basket_delete(id):
    basket = get_basket_by_id(id)
    db.session.delete(basket)
    db.session.commit()

    return basket_schema.jsonify(basket)


if __name__ == '__main__':
    app.run(debug=True)