from typing import List
import numpy as np


class GraphMap:
    """
    Represents a graph map of places in the game.
    Contains a list of places and an adjacency matrix representing connections between them.
    """
    def __init__(self, places_name: List[str], adjacency_matrix):
        """
        Initializes a GraphMap with a list of place names and an adjacency matrix.
        :param places_name: A list of place names.
        :param adjacency_matrix: A 2D numpy array representing the adjacency matrix of the graph.
        """
        self.adjacency_matrix = adjacency_matrix
        self.places_name = places_name
        self.places = []

        for name in places_name:
            place = Place(name)
            self.places.append(place)

        # Add successors and predecessors to each Place
        self.generate_place_adjacency()



    def generate_place_adjacency(self):
        """
        Generates the adjacency relationships between places based on the adjacency matrix.
        This method iterates through the adjacency matrix and sets the successors and predecessors for each place.
        It updates the successors of each place based on the adjacency matrix and also sets the predecessors accordingly
        for each successor.
        :return: None
        """
        for current_place, adjacency in zip(self.places, adjacency_matrix):
            adjacency = np.array(adjacency)
            successor_indices = np.where(adjacency == 1)[0]
            successor_places = [self.places[j] for j in successor_indices]

            current_place.successors = successor_places

            for successor in successor_places:
                successor.add_predecessor(current_place)


    def __repr__(self):
        return f"GraphMap(places={self.places})"



class Place:
    """
    Represents a place in the game.
    """
    def __init__(
            self,
            name: str,
            successors: List['Place'] = None,
            predecessors: List['Place'] = None
    ):
        """
        Initializes a Place with a name, successors, and predecessors.
        :param name: The name of the place.
        :param successors: A list of successor places.
        :param predecessors: A list of predecessor places.
        """
        self.name = name
        self.successors = successors if successors is not None else []
        self.predecessors = predecessors if predecessors is not None else []


    def add_successor(self, place: 'Place'):
        """
        Adds a successor place to the current place.
        Args:
            place (Place): The successor place to add.
        """
        if place not in self.successors:
            self.successors.append(place)



    def add_predecessor(self, place: 'Place'):
        """
        Adds a predecessor place to the current place.
        Args:
            place (Place): The predecessor place to add.
        """
        if place not in self.predecessors:
            self.predecessors.append(place)


    def remove_successor(self, place: 'Place'):
        """
        Removes a successor place from the current place.
        Args:
            place (Place): The successor place to remove.
        """
        if place in self.successors:
            self.successors.remove(place)


    def remove_predecessor(self, place: 'Place'):
        """
        Removes a predecessor place from the current place.
        Args:
            place (Place): The predecessor place to remove.
        """
        if place in self.predecessors:
            self.predecessors.remove(place)


    def __repr__(self):
        return f"Place(name={self.name}, successors={[s.name for s in self.successors]}, predecessors={[p.name for p in self.predecessors]})"
