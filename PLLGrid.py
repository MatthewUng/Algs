try:
    from Tkinter import *
except ImportError:
    from tkinter import *

from BaseGrid import *

class PLLGrid(BaseGrid):
    selected_color = "light goldenrod"

    def __init__(self, master):
        BaseGrid.__init__(self, master)
        self.selected = None
        self.type = None
        self.orientations = None

        self.reset()
        self.setOnClick(self.onObjectClick)

    def onObjectClick(self, event):
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue

                if event.widget.find_closest(event.x, event.y)[0] == self.squares[i][j]:
                    if not self.selected:
                        if is_edge(i, j):
                            self.type = 'e'
                        else:
                            self.type = 'c'

                        self.setSquareColor(i, j, PLLGrid.selected_color)
                        self.selected = [i,j]

                    elif self.selected == [i,j]:
                        self.setSquareColor(i, j, 'yellow')
                        self.selected = None
                        self.type = None

                    elif is_edge(i, j) and self.type == 'e':
                        k, l = self.selected
                        self.setSquareColor(k, l, "yellow")
                        self.swapSquares(i, j, k, l)

                        self.selected = None
                        self.type = None

                    elif is_corner(i, j) and self.type == 'c':
                        k, l = self.selected
                        self.setSquareColor(k, l, "yellow")
                        self.swapSquares(i, j, k, l)

                        self.selected = None
                        self.type = None

                    else: return

    def setPattern(self, pattern):
        pass

    def reset(self):
        self.orientations = [['bo', 'o', 'og'],
                             ['b', None, 'g'],
                             ['rb', 'r', 'gr']]

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

        if self.selected:
            self.setSquareColor(self.selected[0], self.selected[1])
            self.selected = None

    def swapSquares(self, i, j, k, l):
        # swapping orientations
        temp = self.orientations[i][j]
        self.orientations[i][j] = self.orientations[k][l]
        self.orientations[k][l] = temp

        # edge case
        if is_edge(i, j) and is_edge(k, l):
            id1 = self.edges[map_edge(i, j)]
            id2 = self.edges[map_edge(k, l)]
            color = self.itemcget(id1, "fill")
            self.setEdgeColor(map_edge(i, j), self.itemcget(id2, "fill"))
            self.setEdgeColor(map_edge(k, l), color)
            return

        # corner case
        elif is_corner(i, j) and is_corner(k, l):
            id11 = self.corners[map_corner(i, j)][0]
            id12 = self.corners[map_corner(i, j)][1]
            id21 = self.corners[map_corner(k, l)][0]
            id22 = self.corners[map_corner(k, l)][1]

            color1 = self.itemcget(id11, "fill")
            color2 = self.itemcget(id12, "fill")

            self.setCornerColor(map_corner(i, j), 0, self.itemcget(id21, "fill"))
            self.setCornerColor(map_corner(i, j), 1, self.itemcget(id22, "fill"))
            self.setCornerColor(map_corner(k, l), 0, color1)
            self.setCornerColor(map_corner(k, l), 1, color2)

        else:
            print "error in PLLGrid.swapSquares"
            exit()

if __name__ == "__main__":
    root = Tk()
    grid = PLLGrid(root)
    grid.pack()
    # grid.swapSquares(0,0,2,0)
    mainloop()