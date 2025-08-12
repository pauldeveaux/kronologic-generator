from src.game import GraphMap
from src.utils.data_loader import load_game_data

game_data = load_game_data(game=2, language="fr")

places = game_data.places
graph_map = GraphMap(places=places, adjacency_matrix=game_data.adjacency_matrix)
print(graph_map)