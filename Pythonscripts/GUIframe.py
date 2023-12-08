


import tkinter as tk
def mainwindow():
    window = tk.Tk()       # creating the window object
    window.title('my first GUI program')
    window.geometry("800x800")
    window.configure(bg='red')
    #creating the widgets
    Stocknameinput = tk.Entry(window,width=50)
    Stockperiodinput = tk.Entry(window,width =50)
    Stockperiodinput = tk.Entry(window,width =50)
    Stocknamelabel = tk.Label(window, text="please enter the Stock Name in NASDAQ form: ")
    Stockperiodlabel = tk.Label(window,text="please enter the desired period: ")
    Stockfrequencylabel = tk.Label(window,text="please enter the frequency of a sample:")
    Stockfrequencyinput =tk.Entry(window,width = 50)
    enterbutton = tk.Button(window,text="enter data",command=None)
    #placing the objects
    Stocknamelabel.grid(row=1,column =0);Stocknameinput.grid(row=1,column=1)
    Stockperiodlabel.grid(row=2,column=0);Stockperiodinput.grid(row=2,column=1)
    Stockfrequencylabel.grid(row=3,column=0);Stockfrequencyinput.grid(row=3,column=1)
    enterbutton.grid(row=4,column=1)
    window.mainloop()
    #finish the GUI for entry
    #do some data proccesing
    #embed a matplotlib chart inside the tkinter gui
    


# write your code here
mainwindow()