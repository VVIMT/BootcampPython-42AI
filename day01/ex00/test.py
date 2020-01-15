from book import Book
from recipe import Recipe

tourte = Recipe('tourte', '1', '10', 'd', 'e', 'lunch')
to_print = str(tourte)

book = Book(tourte)

book.get_recipes_by_types('dessert')

book.add_recipe(tourte)

book.get_recipes_by_types('dessert')

book.add_recipe(Recipe('jkhjkh', '1', '10', 'd', 'e', 'lunch'))
book.add_recipe(Recipe('222', '1', '10', 'd', 'e', 'dessert'))
book.add_recipe(Recipe('333', '1', '10', 'd', 'e', 'lunch'))


book.get_recipes_by_types('lunch')

print(to_print)

print(book.get_recipe_by_name('snarf')._name)

book.get_recipes_by_types('starter')

