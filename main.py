try:
    from Tkinter import *
except ImportError:
    from tkinter import *

import OLLGrid
import PLLGrid
import cPickle as pickle

def converttotuple(l):
    out = list()
    for List in l:
        out.append(tuple(List))
    return tuple(out)

class MainWindow():
    orientation_OLL_file = r"data/orientations_OLL.p"
    orientation_PLL_file = r"data/orientations_PLL.p"
    algorithms_OLL_file = r"data/algorithms_OLL.p"
    algorithms_PLL_file = r"data/algorithms_PLL.p"
    standard_OLL_file = r"data/standard_OLL.p"
    standard_PLL_file = r"data/standard_PLL.p"

    def __init__(self, master):
        self.master = master
        self.mode = None

        self.title = Label(master, font=("26",))
        self.title.grid(row=0, column=0, columnspan=2, pady=(20,10))

        self.cubegrid = None

        self.strvar = StringVar()
        self.strvar.set("OLL Algorithms")
        self.menu = OptionMenu(master, self.strvar, "OLL Algorithms", "PLL Algorithms", command=self.changeMode)
        self.menu.grid(row=1, column=1, sticky='n', pady=(30,0))

        self.alglabel = Label(master, font=("28",))
        self.alglabel.grid(row=2,column=1, sticky='n', pady=(0,0))

        self.outputtext = Label(master, font=("28",), width=40)
        self.outputtext.grid(row=3, column=1, padx=20, sticky='n', pady=(0,10))

        self.resetButton = Button(master, text="Reset", command=self.reset, font=("14",))
        self.resetButton.grid(row=4, column=0, pady=20)

        self.algsbutton = Button(master, text="submit", command=self.algsOnClick, font=("14",))
        self.algsbutton.grid(row=4, column=1, pady=20)

        self.orientations_OLL = None
        self.orientations_PLL = None
        self.algorithms_OLL = None
        self.algorithms_PLL = None
        self.standard_OLL = None
        self.standard_PLL = None
        self.parsepatterns()

        self.algorithms = None
        self.standard = None
        self.orientations = None

        #self.setUpPLL(master)
        self.setUpOLL(master)

    def setUpOLL(self, master):
        self.mode = "oll"
        self.title.config(text="OLL Algorithms")
        self.cubegrid = OLLGrid.OLLGrid(master)
        self.cubegrid.grid(row=1, column=0, rowspan=3)
        self.algorithms = self.algorithms_OLL
        self.standard = self.standard_OLL
        self.orientations = self.orientations_OLL

    def setUpPLL(self, master):
        self.mode = "pll"
        self.title.config(text="PLL Algorithms")
        self.cubegrid = PLLGrid.PLLGrid(master)
        self.cubegrid.grid(row=1, column=0, rowspan=3)
        self.algorithms = self.algorithms_PLL
        self.standard = self.standard_PLL
        self.orientations = self.orientations_PLL

    def changeMode(self, event):
        if self.strvar.get() == "OLL Algorithms" and self.mode == "pll":
            self.setUpOLL(self.master)
        elif self.strvar.get() == "PLL Algorithms" and self.mode == "oll":
            self.setUpPLL(self.master)
        else:
            pass

    def parsepatterns(self):
        datafile = open(MainWindow.orientation_OLL_file, 'rb')
        s = datafile.read()
        self.orientations_OLL = pickle.loads(s)

        datafile = open(MainWindow.algorithms_OLL_file, 'rb')
        s = datafile.read()
        self.algorithms_OLL = pickle.loads(s)

        datafile = open(MainWindow.standard_OLL_file, 'rb')
        s = datafile.read()
        self.standard_OLL = pickle.loads(s)

        datafile = open(MainWindow.standard_PLL_file, 'rb')
        s = datafile.read()
        self.standard_PLL = pickle.loads(s)

        datafile = open(MainWindow.algorithms_PLL_file, 'rb')
        s = datafile.read()
        self.algorithms_PLL = pickle.loads(s)

        datafile = open(MainWindow.orientation_PLL_file, 'rb')
        s = datafile.read()
        self.orientations_PLL = pickle.loads(s)

    def getgrid(self):
        return self.cubegrid.getValues()

    def algsOnClick(self):
        values = self.getgrid()
        try:
            name = self.orientations[converttotuple(values)]
        except KeyError:
            self.alglabel.config(text="Invalid pattern")
            self.outputtext.config(text="")
            return

        if self.mode == "oll":
            title = "OLL: "+str(name)
        elif self.mode =="pll":
            title = "PLL: "+str(name)

        self.cubegrid.setPattern(self.standard[name])
        self.alglabel.config(text=title)
        outputalgs = self.algorithms[name]
        self.outputtext.config(text=outputalgs)



    def reset(self):
        self.cubegrid.reset()


if __name__ == "__main__":

    top = Tk()
    top.wm_title("Algs")
    window = MainWindow(top)
    mainloop()



