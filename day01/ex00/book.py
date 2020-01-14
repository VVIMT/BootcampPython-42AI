import sys
from recipe import Recipe

class Book(Recipe):
    def __init__(name='', recipes_list={}):
        l1 = []
        l2 = []
        l3 = []
        recipes_list={'starter': l1, 'lunch': l2, 'dessert': l3}
    def get_recipe_by_name(self, name):
        print(name)
        return Recipe
        pass
    def get_recipes_by_types(self, recipe_type):
        recipes_list[Recipe._recipe_type]
        pass
    def add_recipe(self, recipe):
        recipes_list[Recipe._recipe_type].append(Recipe._name)
        pass
