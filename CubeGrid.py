from tkinter import *

class CubeGrid(Canvas):
    squareSize = 100
    edgeSize = 10
    border = 50
    offset = 2

    def __init__(self, master):
        # init values for convenience
        side = CubeGrid.squareSize
        edge = CubeGrid.edgeSize
        bord = CubeGrid.border
        offset = CubeGrid.offset

        wh = 2* bord + 3* side

        Canvas.__init__(self, master,width=wh, height=wh)

        #contains state of the squares (reprensented by ints)
        # 0 1 2
        # 3 4 5
        # 6 4 8
        self.orientation = [[0, 0, 0] for _ in range(3)]

        #contains actual square objects
        self.squares = [[None,None,None] for _ in range(3)]
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

                self.tag_bind(self.squares[i][j], '<ButtonPress-1>', self.onObjectClick)
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

                #corner cases
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



    def flip_edge(self, i, j):
        index = self.map_edge(i, j)
        if self.orientation[i][j] == 0:

            self.itemconfig(self.edges[index], fill="yellow")
            self.itemconfig(self.squares[i][j], fill="grey")
            self.orientation[i][j] = 1

        else:
            self.itemconfig(self.edges[index], fill="grey")
            self.itemconfig(self.squares[i][j], fill="yellow")
            self.orientation[i][j] = 0

    def flip_corner(self, i, j):
        index = self.map_corner(i, j)
        if self.orientation[i][j] == 0:
            self.itemconfig(self.squares[i][j], fill="grey")
            self.itemconfig(self.corners[index][0], fill="yellow")
            self.orientation[i][j] = 1
        elif self.orientation[i][j] == 1:
            self.itemconfig(self.corners[index][0], fill="grey")
            self.itemconfig(self.corners[index][1], fill="yellow")
            self.orientation[i][j] = 2
        elif self.orientation[i][j] == 2:
            self.itemconfig(self.squares[i][j], fill="yellow")
            self.itemconfig(self.corners[index][1], fill="grey")
            self.orientation[i][j] = 0
        else:
            print "error in CubeGrid.flip_corner()"

    def change_orientation(self, input):
        for i in [0, 2]:
            for j in [0,2]:
                while self.orientation[i][j] != input[i][j]:
                    self.flip_corner(i,j)

        for pair in [(0,1), (1,0), (2,1), (1,2)]:
            i = pair[0]
            j = pair[1]
            while self.orientation[i][j] != input[i][j]:
                self.flip_edge(i,j)

    def reset(self):
        temp = [[0,0,0] for _ in range(3)]
        self.change_orientation(temp)

    def map_edge(self, i, j):
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

    def map_corner(self, i, j):
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

    def is_edge(self, i,j):
        if i == 1 and j == 1:
            return False
        elif self.is_corner(i,j):
            return False
        else: return True

    def is_corner(self, i, j ):
        if i == 1 or j == 1:
            return False
        else: return True

    def getValues(self):
        return self.orientation

    def changeValue(self,i,j):
        if self.is_edge(i,j):
            self.flip_edge(i,j)
            return

        elif self.is_corner(i,j):
            self.flip_corner(i,j)
            return
        else:
            print "error in CubeGrid.changeValue()"



    def onObjectClick(self, event):
        #print event.x, event.y
        #print event.widget
        #print event.widget.find_closest(event.x,event.y)
        for i in range(3):
            for j in range(3):
                if event.widget.find_closest(event.x, event.y)[0] == self.squares[i][j]:
                    # center square never changes color

                    if i==1 and j == 1:
                        return

                    self.changeValue(i, j)

                    return


if __name__ == '__main__':
    top = Tk()
    grid = CubeGrid(top)
    grid.pack()
    mainloop()