from tkinter import *
window = Tk()
window.geometry("500x500")
label1 = Label(text = "I am at (0,0)", bg = 'green')
label1.place(x = 0, y = 0)
label2 = Label(text = "I am at (250,250)", bg = 'yellow')
label2.place(x = 250, y = 250)
window.mainloop()