import copy
import random
import tkinter


class Grid:
    def __init__(self, n):
        self._cells = []
        for x in range(n):
            self._cells.append([])
            for _ in range(n):
                # Each cell has a 50% chance of being alive initially.
                self._cells[x].append(random.choice([True, False]))
    
    def cell(self, x, y):
        return self._cells[x][y]

    def update(self):
        # TODO: Refactor this method.
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


n = 50      # num cells in each row/column
size = 12   # cell width/height in pixels

job = None


def play():
    global job
    job = root.after(500, play)
    button.config(text="Pause", command=pause)
    for cell, is_alive in grid.update():
        id = (cell[0] * n) + cell[1] + 1
        if is_alive:
            canvas.itemconfig(id, fill="white")
        else:
            canvas.itemconfig(id, fill="black")


def pause():
    root.after_cancel(job)
    button.config(text="Play", command=play)


# Create the root window.
root = tkinter.Tk()
root.title("Conway's Game of Life")

# Create the grid.
grid = Grid(n)

# Create the canvas.
canvas = tkinter.Canvas(root, width=n*size, height=n*size)
canvas.pack()

# Draw the initial grid to the canvas.
for x in range(n):
    for y in range(n):
        x0 = x * size
        y0 = y * size
        x1 = x0 + size
        y1 = y0 + size
        if grid.cell(x, y):
            color = "white"
        else:
            color = "black"
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)

# Create the play/pause button.
button = tkinter.Button(root, text="Play", command=play)
button.pack(expand=tkinter.YES, fill=tkinter.BOTH)

# Start the Tk event loop.
root.mainloop()