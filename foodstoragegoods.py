from colour import Colour
from material import Material
from country import Country

class FoodStorageGood():
    def __init__(self, size_in_liters=0.0, weight_in_grams=0.0, price_in_uah=0.0, 
                 colour=Colour.TRANSPARENT, material=Material.WOOD, country_of_origin=Country.RUSSIA):
                 print("A new food storage good arrived!")
                 self._size_in_liters = size_in_liters
                 self._weight_in_grams = weight_in_grams
                 self._price_in_uah = price_in_uah
                 self._colour = colour
                 self._country_of_origin = country_of_origin
                 self._material = material

    def __str__(self):
        return f"Size: {self._size_in_liters} l\n"\
               f"Weight: {self._weight_in_grams} g\n"\
               f"Price: {self._price_in_uah} UAH\n"\
               f"Colour: {self._colour.name}\n"\
               f"Manufactured in: {self._country_of_origin.name}\n"\
               f"Material: {self._material.name}"
               
    def __repr__(self):
        return f"Size: {self._size_in_liters} l\n"\
               f"Weight: {self._weight_in_grams} g\n"\
               f"Price: {self._price_in_uah} UAH\n"\
               f"Colour: {self._colour.name}\n"\
               f"Manufactured in: {self._country_of_origin.name}\n"\
               f"Material: {self._material.name}"