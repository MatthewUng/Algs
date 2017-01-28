
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

from BaseGrid import *

class OLLGrid(BaseGrid):

    def __init__(self, master):
        BaseGrid.__init__(self, master)

        self.orientation = [[0,0,0] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.setOnClick(self.onObjectClick)


    def flip_edge(self, i, j):
        index = map_edge(i, j)
        if self.orientation[i][j] == 0:
            self.setEdgeColor(index, "Yellow")
            self.setSquareColor(i, j, "grey")
            self.orientation[i][j] = 1
        else:
            self.setEdgeColor(index, "grey")
            self.setSquareColor(i, j, "yellow")
            self.orientation[i][j] = 0

    def flip_corner(self, i, j):
        index = map_corner(i, j)
        if self.orientation[i][j] == 0:
            self.setSquareColor(i, j, "grey")
            self.setCornerColor(index, 0, "yellow")
            self.orientation[i][j] = 1

        elif self.orientation[i][j] == 1:
            self.setCornerColor(index, 0, "grey")
            self.setCornerColor(index, 1, "yellow")
            self.orientation[i][j] = 2

        elif self.orientation[i][j] == 2:
            self.setCornerColor(index, 1, "grey")
            self.setSquareColor(i, j, "yellow")
            self.orientation[i][j] = 0
        else:
            print "error in OLLGrid.flip_corner()"

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

    def getValues(self):
        return self.orientation

    def changeValue(self,i,j):
        if is_edge(i,j):
            self.flip_edge(i,j)
            return

        elif is_corner(i,j):
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
    grid = OLLGrid(top)
    grid.pack()
    mainloop()