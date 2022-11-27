from recipe_writer import recipe_writer

try:
    recipe_writer.recipe_writer()
except KeyboardInterrupt:
    print("\nExiting...")
    pass