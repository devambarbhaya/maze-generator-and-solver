from graphics import Window
from maze import Maze
import sys

def main():
    # Configure maze dimensions
    num_rows = 50  # Increase the number of rows
    num_cols = 50  # Increase the number of columns
    margin = 50
    screen_x = 1200  # Larger canvas width
    screen_y = 1200   # Larger canvas height

    # Dynamically adjust cell size
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    # Increase recursion limit for large mazes
    sys.setrecursionlimit(20000)

    # Create the window
    win = Window(screen_x, screen_y)

    # Create and solve the maze
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=42)
    print("Maze created")

    # Solve the maze and display the result
    is_solvable = maze.solve()
    if not is_solvable:
        print("Maze cannot be solved")
    else:
        print("Maze solved!")
    
    # Keep the window open until the user closes it
    win.wait_for_close()

main()
