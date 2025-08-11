from src.utils.data_loader import load_characters, load_times


characters, cards = load_characters(2, "fr")
print("Characters loaded successfully:")
for character in cards:
    print(f"Name: {character.name}, Holes Location: {character.holes_location}")


time_cards = load_times(2)
print("\nTime cards loaded successfully:")
for time_card in time_cards:
    print(f"Time: {time_card.name}, Holes Location: {time_card.holes_location}")