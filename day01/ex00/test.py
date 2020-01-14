from book import Book
from recipe import Recipe

tourte = Recipe('tourte', '1', '10', 'd', 'e', 'lunch')
to_print = str(tourte)

print(to_print)
book = Book(tourte)

book.get_recipes_by_types('dessert')

book.add_recipe(tourte)

book.get_recipes_by_types('lunch')
