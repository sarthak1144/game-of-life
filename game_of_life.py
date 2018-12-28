"""
    Bradley Gatewood
    Conway's Game of Life
    December 2019
"""
import copy
import random
import tkinter


class Grid:
    """Create a NxN grid of cells."""
    def __init__(self, n):
        self._cells = []
        for x in range(n):
            self._cells.append([])
            for _ in range(n):
                # Each cell has a 50% chance of being alive initially.
                self._cells[x].append(random.choice([True, False]))
    
    """Return the current state of the cell located at (x,y)."""
    def cell(self, x, y):
        return self._cells[x][y]

    """Update the state of each cell based on the game's rules."""
    def update(self):
        # TODO: Refactor this method.
        # Make it easier to understand and simplify the return data.
        new_cells = copy.deepcopy(self._cells)
        changes = []

        n = len(self._cells)
        for x in range(n):
            for y in range(n):
                lives = self._count_live_neighbors(x, y, n)
                if (self._cells[x][y]):
                    if (lives < 2) or (lives > 3):
                        new_cells[x][y] = False
                        changes.append([(x, y), new_cells[x][y]])
                elif (lives == 3):
                    new_cells[x][y] = True
                    changes.append([(x, y), new_cells[x][y]])
        
        self._cells = new_cells
        return changes

    """Count the number of live neighbors of cell at (x,y)."""
    def _count_live_neighbors(self, x, y, n):
        top = (x - 1) % n
        left = (y - 1) % n
        right = (y + 1) % n
        bottom = (x + 1) % n

        lives = 0
        lives += int(self._cells[top][left])
        lives += int(self._cells[top][y])
        lives += int(self._cells[top][right])
        lives += int(self._cells[x][left])
        lives += int(self._cells[x][right])
        lives += int(self._cells[bottom][left])
        lives += int(self._cells[bottom][y])
        lives += int(self._cells[bottom][right])

        return lives
# end class Grid


class App:
    def __init__(self):
        self.n = 50     # num cells in each row/column
        self.size = 12  # cell width/heigh in pixels
        self.job = None # current job id for root.after()

        # Create the grid.
        self.grid = Grid(self.n)

    def main(self):
        """Create the window and start the main event loop."""
        # TODO: Refactor (shorten) this method.
        # Create the root window.
        self.root = tkinter.Tk()
        self.root.title("Conway's Game of Life")

        # Create the canvas.
        sz = self.n * self.size
        self.canvas = tkinter.Canvas(self.root, width=sz, height=sz)
        self.canvas.pack()

        # Draw the initial grid to the canvas.
        for x in range(self.n):
            for y in range(self.n):
                x0 = x * self.size
                y0 = y * self.size
                x1 = x0 + self.size
                y1 = y0 + self.size
                if self.grid.cell(x, y):
                    color = "white"
                else:
                    color = "black"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        
        # Create the play/pause button.
        self.button = tkinter.Button(self.root, text="Play", command=self.play)
        self.button.pack(expand=tkinter.YES, fill=tkinter.BOTH)

        # Start the Tk event loop.
        self.root.mainloop()

    def play(self):
        """Insert comments here."""
        self.job = self.root.after(500, self.play)
        self.button.config(text="Pause", command=self.pause)
        for cell, is_alive in self.grid.update():
            id = (cell[0] * self.n) + cell[1] + 1 # TODO: Explain this.
            if is_alive:
                self.canvas.itemconfig(id, fill="white")
            else:
                self.canvas.itemconfig(id, fill="black")

    def pause(self):
        """Insert comments here."""
        self.root.after_cancel(self.job)
        self.button.config(text="Play", command=self.play)
# end class App


app = App()
app.main()