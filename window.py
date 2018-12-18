import tkinter


class Window:
    def __init__(self, n, size):
        # n = num cells in each row/column, size = cell width/height in pixels
        self.root = tkinter.Tk()
        self.root.title("Conway's Game of Life")
        self._create_widgets(n, size)

    def update_cell(self, id, is_alive):
        if (is_alive):
            self.canvas.itemconfig(id, fill="white")
        else:
            self.canvas.itemconfig(id, fill="black")
    
    def _create_widgets(self, n, size):
        self.canvas = tkinter.Canvas(self.root, width=n*size, height=n*size)
        self.canvas.pack()
        # Populate the canvas with a NxN grid of dead cells.
        for x in range(n):
            for y in range(n):
                x0 = x * size
                y0 = y * size
                x1 = x0 + size
                y1 = y0 + size
                self._create_cell(x0, y0, x1, y1)
    
    def _create_cell(self, x0, y0, x1, y1):
        # Each cell has a 1px border.
        self.canvas.create_rectangle(x0+1, y0+1, x1-1, y1-1, fill="black")
