from tkinter import *
import sys
nonvicteams = "Brisbane Lions", "Gold Coast Suns", "Sydney Swans", "Greater Western Sydney Giants", "Adelaide Crows", "Port Adelaide Power", "West Coast Eagles", "Fremantle Dockers"
def destroy():
    for child in window.winfo_children():
        child.destroy()
def starting():
    destroy()
    lbl = Label(window, text="""1 = Print all non Victorian Teams
2 = Search for a team in Non Victorian teams
3 = Print the amount of Non Victorian Teams

Which function would you like to use? """, font="none 24 bold", justify=CENTER)
    lbl.config(anchor=CENTER)
    lbl.pack(side=TOP)

    btn1 = Button(window, text="Print all non Victorian Teams", bg="yellow", fg="black", font="none 24 bold", command=btn1click)
    btn2 = Button(window, text="Search for a team in non Victorian Teams", bg="yellow",  fg="black", font="none 24 bold", command=btn2click)
    btn3 = Button(window, text="Print the amount of non Victorian Teams", bg="yellow", fg="black", font="none 24 bold", command=btn3click)
    btn1.config(anchor=CENTER)
    btn2.config(anchor=CENTER)
    btn3.config(anchor=CENTER)
    btn1.pack(side=TOP)
    btn2.pack(side=TOP)
    btn3.pack(side=TOP)
def exit():
    sys.exit("Thank You!")
def btn1click():
    destroy()
    lbl = Label(window, text="""Brisbane Lions
Gold Coast Suns
Sydney Swans
Greater Western Sydney Giants
Adelaide Crows
Port Adelaide Power
West Coast Eagles
Fremantle Dockers""", justify=CENTER)
    lbl2 = Label(window, text="Would you like to try another function?")
    lbl.grid(column=1, row=0)
    lbl2.grid(column=1, row=2)
    btn1 = Button(window, text="Yes", bg="yellow", fg="black", command=starting)
    btn2 = Button(window, text="No", bg="yellow", fg="black", command=exit)
    btn1.grid(column=1, row=3)
    btn2.grid(column=1, row=4)
    #lbl = Label(window, text="Would you like to try another function?")
    #btn1 = Button(window, text="Yes", bg="orange", fg="blue", justify=CENTER, command=btn1click)
    #btn2 = Button(window, text="No", bg="orange", fg="blue", justify=CENTER, command=btn2click)
def btn2click():
    destroy()
    lbl = Label(window, text="button 2 clicked")
    lbl.grid(column=1, row=0)
def btn3click():
    destroy()
    lbl = Label(window, text="button 3 clicked")
    lbl.grid(column=1, row=0)



window = Tk()
window.attributes('-fullscreen', True)
window.configure(background='SteelBlue4')
window.title("AFL Thingo")


lbl = Label(text=" ")
btn1 = Button(text="Print all non Victorian Teams")
btn2 = Button(text="Search for a team in non Victorian Teams")
btn3 = Button(text="Print the amount of non Victorian Teams")
starting()
window.mainloop()