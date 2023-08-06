class ScoreBoard:
    def __init__(self, window):
        self.score = 0
        self.window = window

    def update_score(self, amount: int = 1):
        """Update the score by a certain amount."""
        self.score += amount
        self.window.addstr(0, 0, f'Score: {self.score}')

    def reset_score(self):
        """Reset the score to 0."""
        self.score = 0
        self.window.addstr(0, 0, f'Score: {self.score}')
