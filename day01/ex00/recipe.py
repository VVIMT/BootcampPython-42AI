import sys

class Recipe:
#    name = ''
#    cooking_lvl = 0
#    cooking_time = 0
#    ingredients = []
#    description = ''
#    recipe_type = ''
    _t = ('starter', 'lunch', 'dessert')

    def __init__(self, name='', cooking_lvl=0, cooking_time=0, \
                ingredients=[], description='', recipe_type=''):
        self._name = name
        self._cooking_lvl = cooking_lvl
        self._cooking_time = cooking_time
        self._ingredients = ingredients
        self._description = description
        self._recipe_type = recipe_type

    def __str__(self):
        if (type(self._name) != str):
            sys.exit("Input Error: 'name' must be a string\n")
        if (int(self._cooking_lvl) < 1 or int(self._cooking_lvl) > 5):
            sys.exit("Input Error: 'cooking_lvl' must be between 1 and 5\n")
        if (int(self._cooking_time) < 0):
            sys.exit("Input Error: 'cooking_time' must be a positive number\n")
        for elem in self._ingredients:
            if type(elem) != str:
                sys.exit("Input Error: 'ingredients' must contain strings only\n")
        if (type(self._description) != str):
            sys.exit("Input Error: 'description' must be a string\n")
        if (type(self._recipe_type) != str) or (not (self._recipe_type in self._t)):
            sys.exit("Input Error: 'recipe_type' must be either 'starter', " +\
                    "'lunch' or 'dessert'\n")

        txt = "Recipe" +\
        "\nname:            " + self._name +\
        "\ncooking_lvl:     " + str(self._cooking_lvl) +\
        "\ncooking_time:    " + str(self._cooking_time) +\
        "\ningredients:     " + self._ingredients +\
        "\ndescription:     " + self._description +\
        "\nrecipe_type:     " + self._recipe_type
        return txt
