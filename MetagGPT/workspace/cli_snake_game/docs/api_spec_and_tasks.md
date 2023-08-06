## Required Python third-party packages
```python
"""
curses==2.2
random==1.2.1
"""
```

## Required Other language third-party packages
```python
"""
No third-party packages required.
"""
```

## Full API spec
```python
"""
No API specifications required as this is a CLI based game.
"""
```

## Logic Analysis
```python
[
    ("main.py", "Contains the main entry point of the game. It should call the start_game() method of the Game class."),
    ("game.py", "Contains the Game class. It should control the game flow, including starting and ending the game, controlling the snake and food, and updating the scoreboard."),
    ("snake.py", "Contains the Snake class. It should handle the movement, growth, and collision checking of the snake."),
    ("food.py", "Contains the Food class. It should handle the generation of food coordinates."),
    ("scoreboard.py", "Contains the ScoreBoard class. It should handle the updating of the score.")
]
```

## Task list
```python
[
    "snake.py",
    "food.py",
    "scoreboard.py",
    "game.py",
    "main.py"
]
```

## Shared Knowledge
```python
"""
The 'curses' library is used for creating the CLI interface of the game.
The 'random' library is used for generating the food coordinates.
The game flow is controlled by the Game class in 'game.py'.
The Snake class in 'snake.py' handles the movement, growth, and collision checking of the snake.
The Food class in 'food.py' handles the generation of food coordinates.
The ScoreBoard class in 'scoreboard.py' handles the updating of the score.
"""
```

## Anything UNCLEAR
The requirement is clear. However, we need to ensure that the team is familiar with the 'curses' library for creating the CLI interface. Also, we need to decide on the scoring system, i.e., how much score to increase when the snake eats food.