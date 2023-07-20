from tkinter import *


myroot = Tk()


def select_color_indicator_on_true():
    my_check1['selectcolor'] = 'Green'


def select_color_indicator_on_false():
    my_check2['selectcolor'] = 'Blue'


my_check1 = Checkbutton(myroot, text='CheckButton', command=select_color_indicator_on_true, indicatoron=True)
my_check1.place(x=50, y=50)

my_check2 = Checkbutton(myroot, text='CheckButton', command=select_color_indicator_on_false, indicatoron=False)
my_check2.place(x=50, y=100)

myroot.mainloop()
