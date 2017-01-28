try:
    from Tkinter import *
except ImportError:
    from tkinter import *

from BaseGrid import *

class PLLGrid(BaseGrid):
    def __init__(self, master):
        BaseGrid.__init__(self, master)

        self.orientations = [['BO', 'O', 'OG'],
                             ['B', None, 'G'],
                             ['RB', 'R', 'GR']]

        self.setEdgeColor(0,'orange')
        self.setEdgeColor(1, 'blue')
        self.setEdgeColor(2, 'green')
        self.setEdgeColor(3, 'red')

        self.setCornerColor(0, 0, 'blue')
        self.setCornerColor(0, 1, 'orange')
        self.setCornerColor(1, 0, 'orange')
        self.setCornerColor(1, 1, 'green')
        self.setCornerColor(2, 0, 'red')
        self.setCornerColor(2, 1, 'blue')
        self.setCornerColor(3, 0, 'green')
        self.setCornerColor(3, 1, 'red')




if __name__ == "__main__":
    root = Tk()
    grid = PLLGrid(root)
    grid.pack()
    mainloop()