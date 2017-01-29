try:
    from Tkinter import *
except ImportError:
    from tkinter import *

def map_edge(i, j):
    if i == 1 and j == 0:
        return 0
    elif i == 0 and j == 1:
        return 1
    elif i == 2 and j == 1:
        return 2
    elif i == 1 and j == 2:
        return 3
    else:
        return -1

def map_corner(i, j):
    if i == 0 and j == 0:
        return 0
    elif i == 2 and j == 0:
        return 1
    elif i == 0 and j == 2:
        return 2
    elif i ==2 and j == 2:
        return 3
    else:
        return -1


def is_edge(i,j):
    if i == 1 and j == 1:
        return False
    elif is_corner(i,j):
        return False
    else: return True


def is_corner(i, j ):
    if i == 1 or j == 1:
        return False
    else: return True


class BaseGrid(Canvas):
    squareSize = 100
    edgeSize = 10
    border = 50
    offset = 2

    def __init__(self, master):
        # init values for convenience
        side = BaseGrid.squareSize
        edge = BaseGrid.edgeSize
        bord = BaseGrid.border
        offset = BaseGrid.offset

        wh = 2 * bord + 3 * side
        Canvas.__init__(self, master, width=wh, height=wh)

        # 00 01 02
        # 10 11 12
        # 20 21 22
        self.squares = [[None, None, None] for _ in range(3)]

        #  0
        # 1 2
        #  3
        self.edges = [[] for _ in range(4)]
        # 0 1
        # 2 3
        self.corners = [[] for _ in range(4)]

        for i in range(3):
            for j in range(3):
                x_0 = bord+offset+side*i
                y_0 = bord+offset+side*j
                x_1 = bord-offset+side+side*i
                y_1 = bord-offset+side+side*j

                self.squares[i][j] = self.create_rectangle(x_0, y_0,
                                                           x_1, y_1,
                                                           fill="yellow", tags=str(i)+str(j))

                #self.tag_bind(self.squares[i][j], '<ButtonPress-1>', self.onObjectClick)

                # edge case
                if i == 1 and j == 0:
                    self.edges[0] = self.create_rectangle(x_0, y_0-edge,
                                                          x_1, y_0,
                                                          fill="grey")
                if i==0 and j == 1:
                    self.edges[1] = self.create_rectangle(x_0-edge, y_0,
                                                          x_0, y_1,
                                                          fill="grey")
                if i== 2 and j == 1:
                    self.edges[2] = self.create_rectangle(x_1, y_0,
                                                          x_1+edge, y_1,
                                                          fill="grey")
                if i == 1 and j == 2:
                    self.edges[3] = self.create_rectangle(x_0, y_1,
                                                          x_1, y_1+edge,
                                                          fill="grey")
                # corner cases
                if i == 0 and j == 0:
                    points = [x_0, y_1,
                              x_0, y_0,
                              x_0 - edge, y_0 - edge,
                              x_0 - edge, y_1]
                    temp = self.create_polygon(points, fill="grey", outline="black")
                    self.corners[0].append(temp)

                    points = [x_0, y_0,
                              x_1, y_0,
                              x_1, y_0-edge,
                              x_0-edge, y_0-edge]
                    temp = self.create_polygon(points, fill="grey", outline="black")
                    self.corners[0].append(temp)

                if i == 2 and j == 0:
                    points = [x_0, y_0,
                              x_1, y_0,
                              x_1+edge, y_0-edge,
                              x_0,y_0-edge]
                    temp = self.create_polygon(points, fill="grey", outline="black")
                    self.corners[1].append(temp)

                    points = [x_1,y_0,
                              x_1,y_1,
                              x_1+edge, y_1,
                              x_1+edge, y_0-edge]
                    temp = self.create_polygon(points, fill="grey", outline="black")
                    self.corners[1].append(temp)

                if i == 0 and j == 2:
                    points = [x_0, y_1,
                              x_1, y_1,
                              x_1, y_1 + edge,
                              x_0 - edge, y_1 + edge]
                    temp = self.create_polygon(points, fill="grey", outline="black")
                    self.corners[2].append(temp)

                    points = [x_0, y_0,
                              x_0, y_1,
                              x_0-edge, y_1+edge,
                              x_0-edge, y_0]
                    temp = self.create_polygon(points, fill="grey", outline="black")
                    self.corners[2].append(temp)

                if i == 2 and j == 2:
                    points = [x_1, y_0,
                              x_1+edge, y_0,
                              x_1+edge, y_1+edge,
                              x_1, y_1]
                    temp = self.create_polygon(points, fill="grey", outline="black")
                    self.corners[3].append(temp)

                    points = [x_0, y_1,
                              x_1, y_1,
                              x_1+edge, y_1+edge,
                              x_0, y_1+edge]
                    temp = self.create_polygon(points, fill="grey", outline="black")
                    self.corners[3].append(temp)

    def setOnClick(self, f):
        for i in range(3):
            for j in range(3):
                self.tag_bind(self.squares[i][j], '<ButtonPress-1>', f)

    def setSquareColor(self, i, j, color):
        self.itemconfig(self.squares[i][j], fill=color)

    def setEdgeColor(self, i, color):
        self.itemconfig(self.edges[i], fill=color)

    def setCornerColor(self, i, j, color):
        self.itemconfig(self.corners[i][j], fill=color)


if __name__ == "__main__":
    master = Tk()
    grid = BaseGrid(master)
    grid.pack()
    f = grid.setSquareColor
    grid.setOnClick(grid.onObjectClick)
    mainloop()