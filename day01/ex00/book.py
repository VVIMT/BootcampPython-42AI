import sys
import datetime
from recipe import Recipe

class Book:
    name = ''
    last_update=datetime.datetime.now()
    creation_date=datetime.datetime.now()
    recipes_list = {}

    def __init__(self, Recipe):
        l1 = {}
        l2 = {}
        l3 = {}
        self.recipes_list={'starter': l1, 'lunch': l2, 'dessert': l3}

    def get_recipe_by_name(self, name):
        Recipe._name = name
        return Recipe

    def get_recipes_by_types(self, recipe_type):
        print(self.recipes_list[recipe_type])
        pass

    def add_recipe(self, recipe):
        self.recipes_list[recipe._recipe_type][recipe._name] = recipe
        print(self.recipes_list)
        self.last_update = datetime.datetime.now()
        print(self.last_update)
        print("\n")
        print(self.recipes_list)
        pass
