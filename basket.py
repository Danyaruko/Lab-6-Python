from traditionalfoodstorageitem import TraditionalFoodStorageItem
from utility import Utility
from country import Country
from material import Material
from colour import Colour

class Basket(TraditionalFoodStorageItem):
    def __init__(self, size_in_liters=0.0, weight_in_grams=0.0, price_in_uah=0.0, 
                 colour=Colour.TRANSPARENT, material=Material.WOOD, country_of_origin=Country.RUSSIA,
                 utility=Utility.DECORATIVE, number_of_handles=0):
        super().__init__(size_in_liters, weight_in_grams, price_in_uah, 
                         colour, material, country_of_origin, utility)
        print("It's a basket!")
        self.__number_of_handles = number_of_handles
    
    def __str__(self):
        return f"{super().__str__()}\n"\
               f"Number of handles: {self.__number_of_handles}\n"

    def __repr__(self):
        return f"{super().__repr__()}\n"\
               f"Number of handles: {self.__number_of_handles}\n"
    
    