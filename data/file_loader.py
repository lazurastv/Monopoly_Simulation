import json
from pathlib import Path


class FileLoader:
    matches = None

    def __init__(self):
        if FileLoader.matches is None:
            with open(Path(__file__).parent / "matches.json") as file:
                FileLoader.matches = json.load(file)

    def get(self, datatype):
        filename = self.matches[datatype]
        with open(Path(__file__).parent / (filename + ".json")) as file:
            return json.load(file)
