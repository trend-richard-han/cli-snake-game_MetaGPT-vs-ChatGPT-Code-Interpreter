## snake.py
import curses

class Snake:
    def __init__(self, window, start_coord):
        self.window = window
        self.body = [start_coord]
        self.direction = curses.KEY_RIGHT

    def move(self, direction=None):
        """Move the snake in the given direction, or continue in the current direction if no direction is given."""
        if direction is None:
            direction = self.direction
        else:
            self.direction = direction

        head = self.body[0]
        if direction == curses.KEY_UP:
            new_head = (head[0] - 1, head[1])
        elif direction == curses.KEY_DOWN:
            new_head = (head[0] + 1, head[1])
        elif direction == curses.KEY_LEFT:
            new_head = (head[0], head[1] - 1)
        elif direction == curses.KEY_RIGHT:
            new_head = (head[0], head[1] + 1)

        self.body.insert(0, new_head)
        self.window.addch(new_head[0], new_head[1], '#')

    def grow(self):
        """Grow the snake by not removing the last element after moving."""
        pass

    def check_collision(self):
        """Check if the snake has collided with the border or itself."""
        head = self.body[0]
        if (head in self.body[1:]) or (head[0] in [0, curses.LINES - 1]) or (head[1] in [0, curses.COLS - 1]):
            return True
        return False

    def update(self):
        """Update the display of the snake."""
        self.window.addch(self.body[-1][0], self.body[-1][1], ' ')
        self.window.addch(self.body[0][0], self.body[0][1], '#')
