"""
    Bradley Gatewood
    Conway's Game of Life
    December 2018
"""
import tkinter

from random import choice
from copy import deepcopy


class Grid:
    """Create a NxN grid of cells."""
    def __init__(self, n):
        self._size = n # num cells in each row/column
        self._cells = []
        for x in range(self._size):
            self._cells.append([])
            for _ in range(self._size):
                # Each cell has a 25% chance of being alive initially.
                self._cells[x].append(choice([True, False, False, False]))      # TODO: Is there a better way to do this?
    
    """Return the current state of the cell located at (x,y)."""
    def cell(self, x, y):
        return self._cells[x][y]

    """Update the state of each cell based on the game's rules."""
    def update(self):
        # TODO: Comment.
        self._new_cells = deepcopy(self._cells)
        self._changes = []
        self._update_cells()
        self._cells = self._new_cells
        return self._changes

    # TODO: Update comments.
    def _update_cells(self):
        for x in range(self._size):
            for y in range(self._size):
                lives = self._count_live_neighbors(x, y)
                if self.cell(x, y):
                    if lives < 2 or lives > 3:
                        self._switch_cell(x, y) 
                elif lives == 3:
                    self._switch_cell(x, y)  

    """Count the number of live neighbors for cell at (x,y)."""
    def _count_live_neighbors(self, x, y):
        top = (x - 1) % self._size
        left = (y - 1) % self._size
        right = (y + 1) % self._size
        bottom = (x + 1) % self._size

        lives = 0
        lives += int(self.cell(top, left))
        lives += int(self.cell(top, y))
        lives += int(self.cell(top, right))
        lives += int(self.cell(x, left))
        lives += int(self.cell(x, right))
        lives += int(self.cell(bottom, left))
        lives += int(self.cell(bottom, y))
        lives += int(self.cell(bottom, right))

        return lives

    """Flip the current state of the cell and record the change."""
    def _switch_cell(self, x, y):
        self._new_cells[x][y] = not self._new_cells[x][y]
        self._changes.append([(x, y), self._new_cells[x][y]])
# end class Grid


class App:
    def __init__(self):
        self.n = 50     # num cells in each row/column
        self.cell_size_in_pixels = 12
        self.job = None # current job id for root.after()

        self.grid = Grid(self.n)

    """Initialize the window and start the main event loop."""
    def main(self):
        self._create_widgets()
        self._draw_grid()

        self.root.mainloop()
    
    """Create the window, canvas, and play/pause button."""
    def _create_widgets(self):
        self.root = tkinter.Tk()
        self.root.title("Conway's Game of Life")

        sz = self.n * self.cell_size_in_pixels
        self.canvas = tkinter.Canvas(self.root, width=sz, height=sz)
        self.canvas.pack()
        
        self.button = tkinter.Button(self.root, text="Play", command=self._play)
        self.button.pack(expand=tkinter.YES, fill=tkinter.BOTH)

    """Draw the initial state of the grid to the canvas."""
    def _draw_grid(self):
        for x in range(self.n):
            for y in range(self.n):
                x0 = x * self.cell_size_in_pixels
                y0 = y * self.cell_size_in_pixels
                x1 = x0 + self.cell_size_in_pixels
                y1 = y0 + self.cell_size_in_pixels
                if self.grid.cell(x, y):
                    color = "white"
                else:
                    color = "black"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

    """Start the game."""
    def _play(self):
        self.job = self.root.after(500, self._play)
        self.button.config(text="Pause", command=self._pause)
        for cell, is_alive in self.grid.update():
            id = (cell[0] * self.n) + cell[1] + 1                               # TODO: Explain this.
            if is_alive:
                self.canvas.itemconfig(id, fill="white")
            else:
                self.canvas.itemconfig(id, fill="black")

    """Stop the game."""
    def _pause(self):
        self.root.after_cancel(self.job)
        self.button.config(text="Play", command=self._play)
# end class App


app = App()
app.main()