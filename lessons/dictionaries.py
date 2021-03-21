"""Examples of dictironaries."""

# Establish a type with dict[key type, value type]
# Key type always precedes value type
# Empty dictionary literal is {}
players: dict[str, int] = {}

# Insert a new key-value pair
# Reference keys inside subscription notation, associated values are assigned
players["Brooks"] = 15
players["Love"] = 2
players["Bacot"] = 4 # This is off by one intentionally
players["Bacot"] = players["Bacot"] + 1
print(players)


for player_name in players:
    # player_name is the key in the dictionary
    # values are players[key]
    print(f"{player_name} -> {players[player_name]}")


# You can have keys and values of any types
# This is an example of a dictionary literal
jerseys: dict[int, str] = {15: "Brooks", 2: "Love", 5: "Bacot"}
jerseys[23] = "Jordan"
print(jerseys)
print(jerseys[23])


# The pop method allowes you to remove a key-value pair by its key
# This method return the value associated with the popped key
popped_name: str = jerseys.pop(23)
print(popped_name)
print(jerseys)