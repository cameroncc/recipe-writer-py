from pathlib import Path
from version import RECIPE_WRITER_VERSION

ORDERED = True
UNORDERED = False


class Recipe():
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.directions = []
        self.notes = []

    def set_ingredients(self):
        print("After entering the last ingredient, hit enter twice to finish with ingredients")
        print("Ingredients:")
        self._fill_list(self.ingredients, UNORDERED)
        print()

    def set_directions(self):
        print("After entering the last direction, hit enter twice to finish with directions")
        print("Directions:")
        self._fill_list(self.directions, ORDERED)
        print()

    def set_notes(self):
        do_notes = input("Would you like to add any notes? [Y/n]\n")
        print()
        if do_notes != "N" and do_notes != "n":
            print("After entering the last note, hit enter twice to finish with notes")
            print("Notes:")
            self._fill_list(self.notes, UNORDERED)
            print()

    def write_to_file(self):
        outfilename = self._create_filename(self.name)
        while Path(f"./{outfilename}").exists():
            temp = input(f"File \"{outfilename}\" already exists. Please choose a different name: ")
            outfilename = self._create_filename(temp.replace(".md", ""))

        print(f"Writing recipe for \"{self.name}\" to file \"{outfilename}\"")
        outfile = open(outfilename, 'w')
        outfile.write(f"## {self.name}\n\n### Ingredients\n")
        for item in self.ingredients:
            outfile.write(f"  - {item}\n")

        outfile.write(f"\n### Directions\n")
        count = 1
        for item in self.directions:
            outfile.write(f"  {count}. {item}\n")
            count += 1

        if len(self.notes) != 0:
            outfile.write(f"\n### Notes\n")
            for item in self.notes:
                outfile.write(f"  - {item}\n")

        outfile.write(f"\n[//]: # (Written by recipe-writer-py version {RECIPE_WRITER_VERSION})\n")
        outfile.close()
        print(f"Done writing \"{outfilename}\"\n")

    # Create a filename from recipe name, only allowing alphanumeric chars and '_'
    def _create_filename(self, name):
        filename = ""
        for c in name:
            if not c.isalnum():
                if c == ' ':
                    filename += '_'
            else:
                filename += c

        filename += ".md"
        return filename

    def _fill_list(self, the_list, ordered):
        count = 1
        while True:
            if ordered:
                input_prompt = f"  {count}. "
            else:
                input_prompt = f"  - "

            item = input(input_prompt)
            count += 1
            if item != "":
                the_list.append(item)
            else:
                break
