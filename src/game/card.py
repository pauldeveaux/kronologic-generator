from typing import List
from abc import ABC


class Card(ABC):
    """
    Represents a generic card in the game.
    """
    def __init__(self, name: str):
        """
        Initializes a Card with a given name.
        Args:
            name (str): The name of the card.
        """
        self.name = name



class HolesCard(Card, ABC):
    """
    Represents a card with holes.
    Inherits from Card.
    """
    def __init__(self, name: str, holes_location: List[tuple[int]]):
        super().__init__(name)
        self.holes_location = holes_location



class IconsCard(Card, ABC):
    """
    Represents a card with icons.
    Inherits from Card.
    """
    def __init__(self, name: str, icons: List[List['Icon']]):
        super().__init__(name)
        self.icons = icons



class CharacterCard(HolesCard):
    """
    Represents a character card in the game.
    Inherits from HolesCard.
    """
    def __init__(self, name, holes_location: List[tuple[int]]):
        super().__init__(name, holes_location)



class TimeCard(HolesCard):
    """
    Represents a time card in the game.
    Inherits from Card.
    """
    def __init__(self, time: int, holes_location: List[tuple[int]]):
        name = f"Time {time}"
        super().__init__(name, holes_location)



class PlaceCard(IconsCard):
    """
    Represents a place card in the game.
    Inherits from IconsCard.
    """
    def __init__(self, name: str, icons: List[List['Icon']]):
        super().__init__(name, icons)



class Icon:
    """
    Represents an icon associated with a place card.
    """
    def __init__(self, icon: str):
        self.icon = icon