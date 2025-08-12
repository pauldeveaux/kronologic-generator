import json
import os
from dataclasses import dataclass
from typing import List

from src.game import TimeCard
from src.game.card import CharacterCard, PlaceCard
from src.game.character import Character
from src.game.graph_map import Place

DATA_FOLDER = "data"
CHARACTERS_FOLDER = os.path.join(DATA_FOLDER, "characters")
TIMES_FOLDER = os.path.join(DATA_FOLDER, "times")
PLACES_FOLDER = os.path.join(DATA_FOLDER, "places")



class JsonBadFormatError(Exception):
    """
    Custom exception for handling bad JSON format errors.
    """
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message



def load_characters(game: int, language: str) -> tuple[List[Character], List[CharacterCard]]:
    """
    Loads characters from a file based on the game and language.
    :param game: The game number.
    :param language: The language code.
    :return: A list of Character instances and a list of CharacterCard instances.
    """
    data_folder = CHARACTERS_FOLDER
    trad_folder = os.path.join(data_folder, "languages")

    character_filename = f"characters_kronologic_{game}.json"
    traduction_filename = f"characters_{language}.json"

    try:
        with open(f"{data_folder}/{character_filename}", "r", encoding="utf-8") as file:
            characters_json = json.load(file)
        with open(f"{trad_folder}/{traduction_filename}", "r", encoding="utf-8") as file:
            traduction_json = json.load(file)

        characters_data = characters_json["data"]
        characters_trad = traduction_json["data"]

        # Create CharacterCard instances from the loaded data
        characters_cards: List[CharacterCard] = []
        characters: List[Character] = []
        for character_id in characters_data.keys():
            character_data = characters_data[character_id]
            character_trad = characters_trad[character_id]

            character_card = CharacterCard(
               name=character_trad["name"],
               holes_location=character_data["holes"]
            )
            character = Character(
                name=character_trad["name"],
            )
            characters_cards.append(character_card)
            characters.append(character)

        return characters, characters_cards

    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the files exist in the data directory.")
        raise
    except KeyError as e:
        raise JsonBadFormatError(f"Error: Missing key in JSON data - {e}. Please check the structure of the JSON files.")



def load_times(game: int) -> List[TimeCard]:
    """
    Loads time cards from a file based on the game number.
    :param game: The game number.
    :return: A list of TimeCard instances.
    """
    data_folder = TIMES_FOLDER
    time_filename = f"times_kronologic_{game}.json"

    try:
        with open(f"{data_folder}/{time_filename}", "r", encoding="utf-8") as file:
            times_json = json.load(file)

        times_data = times_json["data"]

        # Create TimeCard instances from the loaded data
        time_cards: List[TimeCard] = []
        for time_id in times_data.keys():
            time_data = times_data[time_id]
            time_card = TimeCard(
                time=int(time_id),
                holes_location=time_data["holes"]
            )
            time_cards.append(time_card)

        return time_cards

    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the file exists in the data directory.")
        raise
    except KeyError as e:
        raise JsonBadFormatError(f"Error: Missing key in JSON data - {e}. Please check the structure of the JSON file.")



def load_places(game: int, language: str) -> tuple[List[Place], List[PlaceCard]]:
    """
    Loads place cards from a file based on the game and language.
    :param game: The game number.
    :param language: The language code.
    :return: A list of Place instances (without their successors) and a list of PlaceCard instances.
    """
    data_folder = PLACES_FOLDER
    trad_folder = os.path.join(data_folder, "languages")

    place_filename = f"places_kronologic_{game}.json"
    traduction_filename = f"places_{language}.json"

    try:
        with open(f"{data_folder}/{place_filename}", "r", encoding="utf-8") as file:
            places_json = json.load(file)
        with open(f"{trad_folder}/{traduction_filename}", "r", encoding="utf-8") as file:
            traduction_json = json.load(file)

        places_data : List[str] = places_json["data"]["places"]
        places_trad = traduction_json["data"]

        # Create PlaceCard instances from the loaded data
        places : List[Place] = []
        places_cards: List[PlaceCard] = []
        for place_id in places_data:
            place_trad = places_trad[place_id]
            place_name = place_trad["name"]

            place = Place(
                name=place_name,
            )
            places.append(place)

            place_card = PlaceCard(
                name=place_trad["name"],
                icons = []
            )
            places_cards.append(place_card)

        return places, places_cards

    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the files exist in the data directory.")
        raise
    except KeyError as e:
        raise JsonBadFormatError(f"Error: Missing key in JSON data - {e}. Please check the structure of the JSON files.")


def load_adjacency_matrix(game: int) -> List[List[int]]:
    """
    Loads the adjacency matrix for the places in the game.
    :param game: The game number.
    :return: A list of lists representing the adjacency matrix.
    """
    data_folder = PLACES_FOLDER
    adjacency_filename = f"places_kronologic_{game}.json"

    try:
        with open(f"{data_folder}/{adjacency_filename}", "r", encoding="utf-8") as file:
            adjacency_json = json.load(file)

        adjacency_matrix = adjacency_json["data"]["adjacency_matrix"]
        return adjacency_matrix

    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the file exists in the data directory.")
        raise
    except KeyError as e:
        raise JsonBadFormatError(f"Error: Missing key in JSON data - {e}. Please check the structure of the JSON file.")



@dataclass
class GameData:
    """
    Represents all the data needed to initialize a game, including characters, places, cards, and adjacency matrix.
    """
    characters: List[Character]
    places: List[Place]
    character_cards: List[CharacterCard]
    time_cards: List[TimeCard]
    place_cards: List[PlaceCard]
    adjacency_matrix: List[List[int]]


def load_game_data(game: int, language: str) -> GameData:
    """
    Loads all game data including characters, places, adjacency matrix, and the cards associated with them.
    :param game: The game number.
    :param language: The language code.
    :return: A GameData instance containing all the loaded data.
    """
    characters, character_cards = load_characters(game, language)
    time_cards = load_times(game)
    places, place_cards = load_places(game, language)
    adjacency_matrix = load_adjacency_matrix(game)

    return GameData(
        characters=characters,
        places=places,
        character_cards=character_cards,
        time_cards=time_cards,
        place_cards=place_cards,
        adjacency_matrix=adjacency_matrix
    )