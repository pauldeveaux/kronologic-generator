from typing import List

from src.game.graph_map import Place


class Character:
    def __init__(self, name: str, locations: List[Place] = None):
        """
        Initializes a Character with a given name and locations.
        Args:
            name (str): The name of the character.
            locations (list): A list of locations associated with the character.
        """
        self.name = name
        self.locations = locations if locations is not None else []


    def random_move(self, start_time: int, previous_time: bool = False):
        if previous_time:
            end_time = start_time - 1
        else:
            end_time = start_time + 1

        #possibles_places = [place for place in self.locations if place.time >= start_time and place.time <= end_time]

