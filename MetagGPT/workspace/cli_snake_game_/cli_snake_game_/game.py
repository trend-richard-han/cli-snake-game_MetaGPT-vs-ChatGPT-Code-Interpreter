import curses
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

class Game:
    def __init__(self, window):
        self.window = window
        self.game_over = False
        self.snake = Snake(self.window, (10, 10))
        self.food = Food(self.window, self.snake)
        self.scoreboard = ScoreBoard(self.window)
        self.delay = 100

    def start_game(self):
        """Start the game."""
        self.window.timeout(self.delay)
        self.snake.move()
        self.food.update()
        self.scoreboard.update_score()

        while not self.game_over:
            self.window.refresh()
            event = self.window.getch()

            if event in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
                self.snake.move(event)
            else:
                self.snake.move()

            if self.snake.check_collision():
                self.game_over = True
            elif self.snake.body[0] == self.food.coordinate:
                self.snake.grow()
                self.scoreboard.update_score()
                self.food = Food(self.window, self.snake)

            self.snake.update()
            self.food.update()

    def end_game(self):
        """End the game and display the final score."""
        self.window.addstr(curses.LINES // 2, curses.COLS // 2, f'Game Over! Final Score: {self.scoreboard.score}')
        self.window.refresh()
        self.window.getch()
