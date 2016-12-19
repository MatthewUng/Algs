from tkinter import *

def motion(event):
    print "Mouse Position: (%s %s)" % (event.x, event.y)
    return

master = Tk()
Whatever_you_do = """Whatever you do will be insignificant, but it is very important that you do
it.\n(Mahatma Gandhi)"""

msg = Message(master, text = Whatever_you_do)
msg.config(bg="lightgreen", font=("times", 24, "italic"))
msg.bind("<Motion>", motion)
msg.pack()

mainloop()
