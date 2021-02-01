from tkinter import *

window = Tk()
window.title("Name of window")
lblwidth = 700
window.geometry("{}x450".format(lblwidth))
window.configure(bg="orange")

# center this label
lbl1 = Label(window, text="List", bg="orange", fg="black", font="none 24 bold",
             width=lblwidth, anchor=CENTER)
lbl1.pack()

lbl2 = Label(window, text="Enter something here:", bg="orange",
             fg="black", font="none 12 bold", width=lblwidth, anchor=W)
lbl2.pack()

window.mainloop()