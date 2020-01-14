import sys

class Recipe:
#    name = ''
#    cooking_lvl = 0
#    cooking_time = 0
#    ingredients = []
#    description = ''
#    recipe_type = ''
    t = ('starter', 'lunch', 'dessert')

    def __init__(self, name='', cooking_lvl=0, cooking_time=0, \
                ingredients=[], description='', recipe_type=''):
        self.n = name
        self.cl = cooking_lvl
        self.ct = cooking_time
        self.i = ingredients
        self.d = description
        self.r = recipe_type

    def __str__(self):
        if (type(self.n) != str):
            sys.exit("Input Error: 'name' must be a string\n")
        if (int(self.cl) < 1 or int(self.cl) > 5):
            sys.exit("Input Error: 'cooking_lvl' must be between 1 and 5\n")
        if (int(self.ct) < 0):
            sys.exit("Input Error: 'cooking_time' must be a positive number\n")
        for elem in self.i:
            if type(elem) != str:
                sys.exit("Input Error: 'ingredients' must contain strings only\n")
        if (type(self.d) != str):
            sys.exit("Input Error: 'description' must be a string\n")
        if (type(self.r) != str) or (not (self.r in self.t)):
            sys.exit("Input Error: 'recipe_type' must be either 'starter', " +\
                    "'lunch' or 'dessert'\n")

        txt = "Recipe" +\
        "\nname:            " + self.n +\
        "\ncooking_lvl:     " + str(self.cl) +\
        "\ncooking_time:    " + str(self.ct) +\
        "\ningredients:     " + self.i +\
        "\ndescription:     " + self.d +\
        "\nrecipe_type:     " + self.r
        return txt
