LOCATIONS = {
    "Beach": {
        "description": "You are standing on a quiet beach. The waves move gently against the shore.",
        "moves": ["Jungle"],
        "item": None,
    },
    "Jungle": {
        "description": "You are inside a thick jungle. You notice a rope lying near a tree.",
        "moves": ["Beach", "Cave"],
        "item": "Rope",
    },
    "Cave": {
        "description": "You have entered a dark cave. A lantern rests on a stone.",
        "moves": ["Jungle", "Old Bridge"],
        "item": "Lantern",
    },
    "Old Bridge": {
        "description": "An old bridge connects the cave to the lighthouse. It looks dangerous.",
        "moves": ["Cave", "Lighthouse"],
        "item": None,
    },
    "Lighthouse": {
        "description": "You have reached the lighthouse. The island's beacon can be lit here.",
        "moves": ["Old Bridge"],
        "item": None,
    },
}


def new_game(name):
    return {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False,
    }


def available_moves(player):
    return LOCATIONS[player["location"]]["moves"]


def can_cross_bridge(player):
    return "Rope" in player["inventory"]


def move_player(player, destination):
    destination = destination.strip().title()

    if player["game_over"]:
        return False, "The game is already over."

    if destination not in available_moves(player):
        return False, "You cannot move there from your current location."

    if destination == "Old Bridge" and player["location"] == "Cave":
        if not can_cross_bridge(player):
            return False, "The bridge is unsafe. You need a rope."

    if destination == "Lighthouse" and player["location"] == "Old Bridge":
        if not can_cross_bridge(player):
            return False, "The bridge is unsafe. You need a rope."

    player["location"] = destination
    player["energy"] -= 1

    if player["energy"] <= 0:
        player["energy"] = 0
        player["game_over"] = True
        player["won"] = False
        return True, "You have run out of energy!"

    return True, f"You moved to {destination}."


def pickup_item(player):
    location = player["location"]
    item = LOCATIONS[location]["item"]

    if item is None:
        return False, "There is nothing to collect here."

    if item in player["inventory"]:
        return False, f"You already collected the {item.lower()}."

    player["inventory"].append(item)

    return True, f"You collected the {item.lower()}."


def show_inventory(player):
    if not player["inventory"]:
        return "Your inventory is empty."

    return "You are carrying: " + ", ".join(player["inventory"])


def can_light_beacon(player):
    return (
        player["location"] == "Lighthouse"
        and "Lantern" in player["inventory"]
        and not player["game_over"]
    )


def light_beacon(player):
    if player["game_over"]:
        return False, "The game is already over."

    if player["location"] != "Lighthouse":
        return False, "You must be at the lighthouse to light the beacon."

    if "Lantern" not in player["inventory"]:
        return False, "You need a lantern to light the beacon."

    player["game_over"] = True
    player["won"] = True

    return True, "You light the beacon! A rescue ship sees the signal. You win!"


def is_win(player):
    return player["won"]


def is_loss(player):
    return player["game_over"] and not player["won"]


def describe_location(player):
    location = player["location"]
    return LOCATIONS[location]["description"]
