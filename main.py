try:
    from Tkinter import *
except ImportError:
    from tkinter import *

import OLLGrid
import cPickle as pickle

def converttotuple(l):
    out = list()
    for List in l:
        out.append(tuple(List))
    return tuple(out)

class MainWindow():
    orientation_data_file = r"data/orientations_OLL.p"
    OLL_algorithm_data = r"data/algorithms_OLL.p"
    standard_orientation_file = r"data/standard_OLL.p"

    def __init__(self, master):
        self.title = Label(master, text="OLL Algorithms", font=("26",))
        self.title.grid(row=0, column=0, columnspan=2, pady=10)

        self.cubegrid = OLLGrid.OLLGrid(master)
        self.cubegrid.grid(row=1, column=0, rowspan=2)

        self.olllabel = Label(master, font=("28",))
        self.olllabel.grid(row=1,column=1)

        self.outputtext = Label(master, font=("28",), width=40)
        self.outputtext.grid(row=2, column=1, padx=20, sticky='n')

        self.resetButton = Button(master, text="Reset", command=self.cubegrid.reset, font=("14",))
        self.resetButton.grid(row=3, column=0, pady=20)

        self.algsbutton = Button(master, text="submit", command=self.algsOnClick, font=("14",))
        self.algsbutton.grid(row=3, column=1, pady=20)

        self.OLL_pattern_dict = None
        self.OLL_algorithms = None
        self.OLL_standard = None
        self.parsepatterns()

        # self.getgrid()

    def parsepatterns(self):
        datafile = open(MainWindow.orientation_data_file, 'rb')
        s = datafile.read()
        self.OLL_pattern_dict = pickle.loads(s)

        datafile = open(MainWindow.OLL_algorithm_data, 'rb')
        s = datafile.read()
        self.OLL_algorithms = pickle.loads(s)

        datafile = open(MainWindow.standard_orientation_file, 'rb')
        s = datafile.read()
        self.OLL_standard = pickle.loads(s)

    def getgrid(self):
        return self.cubegrid.getValues()

    def algsOnClick(self):
        values = self.getgrid()
        try:
            ollnumber = self.OLL_pattern_dict[converttotuple(values)]
        except KeyError:
            self.olllabel.config(text="Invalid pattern")
            self.outputtext.config(text="")
            return

        olltext = "OLL: " + str(ollnumber)
        self.olllabel.config(text=olltext)

        outputalgs = self.OLL_algorithms[ollnumber]
        self.outputtext.config(text=outputalgs)
        self.cubegrid.change_orientation(self.OLL_standard[ollnumber])

if __name__ == "__main__":

    top = Tk()
    top.wm_title("Algs")
    window = MainWindow(top)
    mainloop()



