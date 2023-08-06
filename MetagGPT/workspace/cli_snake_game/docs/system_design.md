## Implementation approach
The game will be implemented using Python's built-in libraries such as curses for the CLI interface and random for the food generation. The game will have a main loop that will keep the game running until the player loses. The snake will be a list of coordinates that will move in a certain direction based on the player's input. The food will be a randomly generated coordinate that the snake can eat to increase its length. The score will be calculated based on the length of the snake. The difficulty will increase by decreasing the delay between each move of the snake as the score increases.

## Python package name
```python
"cli_snake_game"
```

## File list
```python
[
    "main.py",
    "game.py",
    "snake.py",
    "food.py",
    "scoreboard.py"
]
```

## Data structures and interface definitions
```mermaid
classDiagram
    class Game{
        +bool game_over
        +int delay
        +start_game()
        +end_game()
    }
    class Snake{
        +list coordinates
        +str direction
        +move()
        +grow()
        +check_collision()
    }
    class Food{
        +tuple coordinate
        +generate()
    }
    class ScoreBoard{
        +int score
        +update_score()
    }
    Game "1" -- "1" Snake: controls
    Game "1" -- "1" Food: controls
    Game "1" -- "1" ScoreBoard: updates
```

## Program call flow
```mermaid
sequenceDiagram
    participant M as Main
    participant G as Game
    participant S as Snake
    participant F as Food
    participant SB as ScoreBoard
    M->>G: start_game()
    loop game not over
        G->>S: move()
        G->>S: check_collision()
        alt snake eats food
            G->>F: generate()
            G->>S: grow()
            G->>SB: update_score()
        end
    end
    G->>M: end_game()
```

## Anything UNCLEAR
The requirement is clear to me.