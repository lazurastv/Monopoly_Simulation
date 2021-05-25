import json


class FileLoader:
    matches = None

    def __init__(self):
        if FileLoader.matches is None:
            with open("matches.json") as file:
                FileLoader.matches = json.load(file)

    def get(self, datatype):
        filename = self.matches[datatype]
        with open(filename + ".json") as file:
            return json.load(file)
