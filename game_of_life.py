"""
    Bradley Gatewood
    Conway's Game of Life
    December 2018
"""
import tkinter

from random import choices
from copy import deepcopy


class Grid:

    """Create a NxN grid of cells. True == ALIVE, False == DEAD"""
    def __init__(self, n):
        self._size = n # num cells in each row/column
        self._cells = []

        values = [True, False]
        weights = [0.25, 0.75]

        for x in range(self._size):
            self._cells.append([])
            for _ in range(self._size):
                self._cells[x].append(choices(values, weights)) 
    

    """Return the current state of the cell located at (x,y)."""
    def cell(self, x, y):
        return self._cells[x][y]


    """Update the state of the grid."""
    def update(self):
        self._new_cells = deepcopy(self._cells)
        self._changed_cells = []

        self._update_cells()

        self._cells = self._new_cells
        return self._changed_cells


    """Update the state of each cell based on the game's rules."""
    def _update_cells(self):
        for x in range(self._size):
            for y in range(self._size):
                lives = self._count_live_neighbors(x, y)
                if self.cell(x, y):
                    if lives < 2 or lives > 3:
                        self._switch_cell(x, y) 
                elif lives == 3:
                    self._switch_cell(x, y)
    
    
    """Flip the current state of the cell and record the change."""
    def _switch_cell(self, x, y):
        self._new_cells[x][y] = not self._new_cells[x][y]
        self._changed_cells.append((x, y))


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
# end class Grid


class App:
    def __init__(self):
        self._n = 50     # num cells in each row/column
        self._cell_size_in_pixels = 12
        self._current_job = None

        self._grid = Grid(self._n)


    """Initialize the window and start the main event loop."""
    def main(self):
        self._create_window()
        self._draw_grid()

        self._root.mainloop()
    

    """Create the window, canvas, and play/pause button."""
    def _create_window(self):
        self._root = tkinter.Tk()
        self._root.title("Conway's Game of Life")

        sz = self._n * self._cell_size_in_pixels
        self._canvas = tkinter.Canvas(self._root, width=sz, height=sz)
        self._canvas.pack()
        
        self._btn = tkinter.Button(self._root, text="Play", command=self._play)
        self._btn.pack(expand=tkinter.YES, fill=tkinter.BOTH)


    """Draw the initial state of the grid to the canvas."""
    def _draw_grid(self):
        for x in range(self._n):
            for y in range(self._n):
                x0 = x * self._cell_size_in_pixels
                y0 = y * self._cell_size_in_pixels
                x1 = x0 + self._cell_size_in_pixels
                y1 = y0 + self._cell_size_in_pixels
                # TODO: Change fill colors to class members.
                if self._grid.cell(x, y):
                    color = "white"
                else:
                    color = "black"
                self._canvas.create_rectangle(x0, y0, x1, y1, fill=color)


    """Start the game."""
    def _play(self):
        self._current_job = self._root.after(500, self._play)
        self._btn.config(text="Pause", command=self._pause)
        for cell in self._grid.update():
            x, y = cell
            id = (x * self._n) + y + 1 # TODO: Explain this.
            # TODO: Change fill colors to class members.
            if self._grid.cell(x, y):
                self._canvas.itemconfig(id, fill="white")
            else:
                self._canvas.itemconfig(id, fill="black")


    """Stop the game."""
    def _pause(self):
        self._root.after_cancel(self._current_job)
        self._btn.config(text="Play", command=self._play)
# end class App


app = App()
app.main()