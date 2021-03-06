#!/usr/bin/env python3

from Recipe import Recipe
from version import RECIPE_WRITER_VERSION

def main():
    print("Welcome to recipe writer!")
    print(f"Version: {RECIPE_WRITER_VERSION}\n")

    create_recipe = True
    while create_recipe:
        print("Creating new recipe")
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
        if do_another == "N" or do_another == "n":
            create_recipe = False

if __name__ == "__main__":
    main()
