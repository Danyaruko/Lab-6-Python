from foodstoragegoods import FoodStorageGood
from utility import Utility
from country import Country
from material import Material
from colour import Colour

class TraditionalFoodStorageItem(FoodStorageGood):
    def __init__(self, size_in_liters=0.0, weight_in_grams=0.0, price_in_uah=0.0, 
                 colour=Colour.TRANSPARENT, material=Material.WOOD, 
                 country_of_origin=Country.RUSSIA, utility=Utility.DECORATIVE):
        super().__init__(size_in_liters, weight_in_grams, price_in_uah, 
                         colour, material, country_of_origin)
        print("It's a traditional one!")
        self._utility = utility
        
    def __str__(self):
        return f"{super().__str__()}\n"\
               f"Utility: {self._utility.name}"
    
    def __repr__(self):
        return f"{super().__repr__()}\n"\
               f"Utility: {self._utility.name}"
