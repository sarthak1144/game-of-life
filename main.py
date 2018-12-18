from grid import Grid
import tkinter


class Window:
    def __init__(self, n, size):
        # n = num cells in each row/column
        # size = cell width/height in pixels
        self.root = tkinter.Tk()
        self.root.title("Conway's Game of Life")

        # Create the canvas.
        self.canvas = tkinter.Canvas(self.root, width=n*size, height=n*size)
        self.canvas.pack()

        # Create a NxN grid of dead cells.
        for x in range(n):
            for y in range(n):
                x0 = x * size
                y0 = y * size
                x1 = x0 + size
                y1 = y0 + size
                # Each cell has a 1px border.
                self.canvas.create_rectangle(x0+1, y0+1, x1-1, y1-1,
                                             fill="black")


class Application:
    def __init__(self):
        self.N = 50 # num cells in each row/column
        self.SIZE = 12 # cell width/height in pixels
        self.grid = Grid(self.N)
        self.window = Window(self.N, self.SIZE)
    
    def update(self):
        self.grid.update()

        for x in range(self.N):
            for y in range(self.N):
                if (self.grid._cells[x][y]):
                    self.window.canvas.itemconfig(x * self.N + y + 1, fill="white")
                else:
                    self.window.canvas.itemconfig(x * self.N + y + 1, fill="black")

        self.window.root.after(250, self.update)


app = Application()
app.update()
app.window.root.mainloop() # Why does this need to be here?!