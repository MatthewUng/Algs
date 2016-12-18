from tkinter import *

class CubeGrid(Canvas):
    squareSize = 150
    offset = 5
    def __init__(self, master, w=600, h=600):
        Canvas.__init__(self, master,width=w, height=h)
        self.grid = [[True, True, True] for _ in range(3)]
        self.squares = [[0,0,0] for _ in range(3)]
        for i in range(3):
            for j in range(3):

                self.squares[i][j] = self.create_rectangle(105+Canvas.squareSize*i, 105+Canvas.squareSize*j,
                                                           245+Canvas.SquareSize*i, 245+Canvas.squareSize*j,
                                                           fill="yellow", tags=str(i)+str(j))
                self.tag_bind(self.squares[i][j], '<ButtonPress-1>', self.onObjectClick)

        self.pack()

    def getValues(self):
        return self.grid

    def changeValue(self,i,j):

        self.grid[i][j] = not self.grid[i][j]
        print self.getValues()


    def onObjectClick(self, event):
        print event.x, event.y
        print event.widget
        print event.widget.find_closest(event.x,event.y)


if __name__ == '__main__':
    top = Tk()
    CubeGrid(top)
    mainloop()