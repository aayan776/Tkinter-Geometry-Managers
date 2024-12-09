from tkinter import *
window = Tk()
window.title("Sample frame")
window.geometry("400x300")
border_effects = [FLAT, SUNKEN, RAISED, GROOVE, RIDGE]
for i in border_effects:
    frame = Frame(master = window, relief = i, borderwidth = 5)
    frame.pack(side = LEFT)
    label = Label(master = frame, text = i)
    label.pack()