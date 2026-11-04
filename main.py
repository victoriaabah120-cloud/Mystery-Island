from game import (
    new_game,
    available_moves,
    move_player,
    pickup_item,
    show_inventory,
    light_beacon,
    describe_location,
    is_win,
    is_loss,
)


def show_status(player):
    print("\n" + "=" * 40)
    print(f"Player: {player['name']}")
    print(f"Location: {player['location']}")
    print(f"Energy: {player['energy']}")
    print("=" * 40)


def show_menu():
    print("\nWhat would you like to do?")
    print("1. Move")
    print("2. Collect item")
    print("3. Check inventory")
    print("4. Look around")
    print("5. Light the beacon")
    print("6. Quit")


def play_game():
    print("=" * 40)
    print("       MYSTERY ISLAND")
    print("=" * 40)
    print("Find the items you need and light the lighthouse beacon.")
    print("You have limited energy, so plan your moves carefully.")
    print("You need a rope to cross the old bridge.")
    print("You need a lantern to light the beacon.")

    name = input("\nWhat is your name? ").strip()

    if not name:
        name = "Explorer"

    player = new_game(name)

    print(f"\nWelcome, {player['name']}!")
    print(describe_location(player))

    while not player["game_over"]:
        show_status(player)
        show_menu()

        choice = input("\nEnter your choice: ").strip().lower()

        if choice in ("1", "move"):
            print("\nAvailable destinations:")

            for destination in available_moves(player):
                print(f"- {destination}")

            destination = input("Where do you want to go? ").strip()

            success, message = move_player(player, destination)
            print(message)

            if success and not player["game_over"]:
                print(describe_location(player))

        elif choice in ("2", "collect", "pickup"):
            success, message = pickup_item(player)
            print(message)

        elif choice in ("3", "inventory", "i"):
            print(show_inventory(player))

        elif choice in ("4", "look"):
            print(describe_location(player))

        elif choice in ("5", "light"):
            success, message = light_beacon(player)
            print(message)

        elif choice in ("6", "quit", "exit"):
            print("You have left the island adventure.")
            player["game_over"] = True

        else:
            print("Invalid choice. Please choose a number from 1 to 6.")

    if is_win(player):
        print("\nCongratulations! You completed the adventure.")
    elif is_loss(player):
        print("\nGame over. You ran out of energy.")
    else:
        print("\nThanks for playing Mystery Island!")


def main():
    while True:
        play_game()

        replay = input("\nWould you like to play again? (yes/no): ").strip().lower()

        if replay not in ("yes", "y"):
            print("Thanks for playing Mystery Island!")
            break


if __name__ == "__main__":
    main()
