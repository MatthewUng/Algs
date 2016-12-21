from tkinter import *
import CubeGrid
import cPickle as pickle

class MainWindow():
    orientation_data_file = r"orientation_data.p"

    def __init__(self, master):
        self.title = Label(master, text="OLL Algorithms", font=("26",))
        self.title.grid(row=0, column=0, columnspan=2, pady=10)

        self.cubegrid = CubeGrid.CubeGrid(master)
        self.cubegrid.grid(row=1, column=0, rowspan=2)

        self.outputtext = Label(master, font=("28",))
        self.outputtext.grid(row=1, column=1)

        self.algsbutton = Button(master, text="submit", command=self.algsOnClick)
        self.algsbutton.grid(row=2, column=1, padx=120)

        self.hash = None
        self.parsepatterns()

        self.getgrid()


    def parsepatterns(self):
        datafile = open(MainWindow.orientation_data_file, 'rb')
        s = datafile.read()
        self.hash = pickle.loads(s)

    def getgrid(self):
        return self.cubegrid.getValues()

    def algsOnClick(self):
        print "clicked"
        values = self.getgrid()
        for line in values:
            print line

        outputalgs = """R U R' U R d' R U' R' F'
R' U' R U' R' d R' U R B
R' U' R U' R' U F' U F R
R U R' U R U' y R U' R' F'"""
        self.outputtext.config(text=outputalgs)

if __name__ == "__main__":

    top = Tk()
    window = MainWindow(top)
    mainloop()



