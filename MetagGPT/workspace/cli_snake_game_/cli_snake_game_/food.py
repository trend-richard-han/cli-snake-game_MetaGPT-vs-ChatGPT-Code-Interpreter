import random
import curses

class Food:
    def __init__(self, window, snake):
        self.window = window
        self.snake = snake
        self.coordinate = self.generate()

    def generate(self):
        """Generate a new food coordinate."""
        while True:
            coordinate = (random.randint(1, curses.LINES - 2), random.randint(1, curses.COLS - 2))
            if coordinate not in self.snake.body:
                return coordinate

    def update(self):
        """Update the display of the food."""
        self.window.addch(self.coordinate[0], self.coordinate[1], '*')
