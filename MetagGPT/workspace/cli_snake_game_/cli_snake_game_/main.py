import curses
from game import Game

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    game = Game(stdscr)
    game.start_game()

    while True:
        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == ord('n'):
            game = Game(stdscr)
            game.start_game()

        game.end_game()

if __name__ == "__main__":
    curses.wrapper(main)
