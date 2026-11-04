# 🏝️ Mystery Island

**Mystery Island** is a text-based adventure game built with Python. The player is stranded on a mysterious island and must explore different locations, collect useful items, manage limited energy, and light a lighthouse beacon to signal a rescue ship.

The project demonstrates fundamental Python programming concepts, including variables, dictionaries, functions, conditionals, loops, user input, and automated testing.

## 🎮 Game Overview

You begin your adventure on a quiet beach with only 5 energy points.

To escape the island, you must:
- Explore the island's different locations.
- Collect a rope and a lantern.
- Use the rope to cross the old bridge.
- Reach the lighthouse.
- Light the beacon to win the game.

Be careful! Every successful move costs 1 energy point.

## 🗺️ Island Map

```text
        BEACH
          |
        JUNGLE
          |
         CAVE
          |
      OLD BRIDGE
          |
      LIGHTHOUSE
```

## 🧰 Items

| Item | Location | Purpose |
|---|---|---|
| Rope | Jungle | Allows you to cross the old bridge |
| Lantern | Cave | Allows you to light the lighthouse beacon |

## ✨ Features

- Interactive command-line gameplay
- Multiple locations to explore
- Inventory system for collecting items
- Energy management system
- Location-based movement
- Conditional game progression
- Winning and losing conditions
- Replay option
- Automated unit tests using Python's built-in `unittest` module

## 🛠️ Technologies Used

- Python 3.10+
- Python `unittest`
- Git
- GitHub

No external Python packages are required.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Mystery-Island.git
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Navigate to the project directory

```bash
cd Mystery-Island
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the virtual environment

Linux/macOS:

```bash
source .venv/bin/activate
```

### 5. Run the game

```bash
python main.py
```

## 🧪 Running the Tests

The project includes automated tests to verify the game mechanics.

Run:

```bash
python -m unittest discover -s tests -v
```

The tests cover:
- Initial game state
- Player movement
- Energy reduction
- Item collection
- Bridge restrictions
- Inventory requirements
- Beacon activation
- Winning and losing conditions

## 🎯 How to Play

When the game starts, enter your name.

Use the menu to choose an action:

| Option | Action |
|---|---|
| 1 | Move |
| 2 | Collect an item |
| 3 | Check inventory |
| 4 | Look around |
| 5 | Light the beacon |
| 6 | Quit |

## 🏆 Winning Strategy

1. Start at the Beach.
2. Move to the Jungle.
3. Collect the Rope.
4. Move to the Cave.
5. Collect the Lantern.
6. Move to the Old Bridge.
7. Cross to the Lighthouse.
8. Light the beacon.

If you manage your energy correctly, you will signal a rescue ship and win the adventure.

## 📁 Project Structure

```text
Mystery-Island/
│
├── main.py
├── game.py
├── README.md
├── .gitignore
│
└── tests/
    ├── __init__.py
    └── test_game.py
```

## 📚 Learning Objectives

This project was created to practice and strengthen Python programming skills, including:

- Variables and data types
- Dictionaries and lists
- Functions
- Conditional statements
- Loops
- User input and output
- Modular programming
- Error handling
- Unit testing
- Git and GitHub workflow

## 🔮 Future Improvements

Possible future enhancements include:

- More island locations
- Additional items and puzzles
- Random events
- More complex challenges
- A graphical user interface
- Save and
