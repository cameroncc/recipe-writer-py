from .models.Recipe import Recipe
from .version import RECIPE_WRITER_VERSION


def recipe_writer():
    print("Welcome to recipe writer!")
    print(f"Version: {RECIPE_WRITER_VERSION}\n")

    create_recipe = True
    while create_recipe:
        print("Creating new recipe")
        name = ""
        while not name:
            name = input("Name: ")

        recipe = Recipe(name)
        print()

        recipe.set_ingredients()
        print()
        recipe.set_directions()
        print()
        recipe.set_notes()
        print()
        recipe.write_to_file()

        do_another = input("Would you like to add another recipe? [Y/n] ")
        create_recipe = do_another.lower() != "n"
