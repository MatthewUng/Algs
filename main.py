from tkinter import *
import CubeGrid
import cPickle as pickle

class MainWindow():
    orientation_data_file = r"orientation_data.p"

    def __init__(self, master):
        print "here"
        self.title = Label(master, text="OLL Algorithms")
        self.title.pack(ipady="10")

        self.grid = CubeGrid.CubeGrid(master)
        self.grid.pack(side=LEFT)

        self.outputtext = Label(master)
        self.outputtext.pack(side=RIGHT)

        self.algsbutton = Button(master, text="submit", command=self.algsOnClick)
        self.algsbutton.pack(padx="20", side=RIGHT)

        self.hash = None
        self.parsepatterns()

        self.getgrid()


    def parsepatterns(self):
        datafile = open(MainWindow.orientation_data_file, 'rb')
        s = datafile.read()
        self.hash = pickle.loads(s)

    def getgrid(self):
        return self.grid.getValues()

    def algsOnClick(self):
        print "clicked"
        values = self.getgrid()
        for line in values:
            print line

        outputalgs = "put algs here"
        self.outputtext.config(text=outputalgs)

if __name__ == "__main__":

    top = Tk()
    window = MainWindow(top)
    mainloop()



