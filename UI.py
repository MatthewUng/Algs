from tkinter import *

class CubeGrid(Canvas):
    squareSize = 150
    edgeSize = 25
    border = 50
    offset = 5

    def __init__(self, master):
        # init values for convenience
        side = CubeGrid.squareSize
        edge = CubeGrid.edgeSize
        bord = CubeGrid.border
        offset = CubeGrid.offset

        wh = 2* bord + 3* side

        Canvas.__init__(self, master,width=wh, height=wh)


        self.grid = [[0, 0, 0] for _ in range(3)]
        #
        self.squares = [[0,0,0] for _ in range(3)]
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
                    self.edges[0] = self.create_rectangle(bord + offset + side * i, bord + offset + side * j - edge,
                                                          bord - offset + side + side * i, bord + offset + side * j,
                                                          fill="black")
                if i==0 and j == 1:
                    self.edges[1] = self.create_rectangle(bord+offset+side*i-edge, bord+offset+side*j,
                                                          bord+side*i+offset, bord-offset+side+side*j,
                                                          fill="black")
                if i== 2 and j == 1:
                    self.edges[2] = self.create_rectangle(bord-offset+side+side*i, bord+offset+side*j,
                                                          bord-offset+side+side*i+edge, bord-offset+side+side*j,
                                                          fill="black")
                if i == 1 and j == 2:
                    self.edges[3] = self.create_rectangle(bord+offset+side*i, bord-offset+side+side*j,
                                                          bord-offset+side+side*i, bord-offset+side+side*j+edge,
                                                          fill="black")

                #corner cases
                if i == 0 and j == 0:
                    points = [x_0, y_0,
                              x_1, y_0,
                              x_1, y_0-edge,
                              x_0-edge, y_0-edge]
                    temp1 = self.create_polygon(points, fill="black")
                    self.corners[0].append(temp1)

                if i == 2 and j == 0:
                    points = [x_0, y_0,
                              x_1, y_0,
                              x_1+edge, y_0-edge,
                              x_0,y_0-edge]
                    temp = self.create_polygon(points, fill="black")
                    self.corners[1].append(temp)


        self.pack()

    def is_edge(self, i,j):
        if i == 1 and j == 1:
            return False
        elif self.is_corner(i,j):
            return False
        else: return True

    def is_corner(self, i, j ):
        if i!= 0 or i != 2 or j != 0 or j!= 2:
            return False
        else: return True

    def getValues(self):
        return self.grid

    def changeValue(self,i,j):
        if self.itemcget(self.squares[i][j], "fill") == "yellow":

            self.itemconfig(self.squares[i][j], fill="black")
        else:
            self.itemconfig(self.squares[i][j], fill="yellow")

        # edges have 2 orientations
        if i != 0 or i != 2 or j != 0 or j != 2:
            self.grid[i][j] = (self.grid[i][j] + 1) % 2
        # corners have 3 orientations
        else:
            self.grid[i][j] = (self.grid[i][j] + 1) % 3


    def onObjectClick(self, event):
        #print event.x, event.y
        #print event.widget
        #print event.widget.find_closest(event.x,event.y)
        for i in range(3):
            for j in range(3):
                if event.widget.find_closest(event.x, event.y)[0] == self.squares[i][j]:
                    if i==1 and j == 1:
                        return

                    self.changeValue(i, j)

                    return


if __name__ == '__main__':
    top = Tk()
    CubeGrid(top)
    mainloop()