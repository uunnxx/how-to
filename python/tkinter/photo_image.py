from tkinter import *


root = Tk()

on_image = PhotoImage(width=50, height=25)
off_image = PhotoImage(width=50, height=25)
on_image.put(('Green',), to=(0, 0, 24, 24))
off_image.put(('Red',), to=(25, 0, 49, 24))

val1 = IntVar(value=0)
val2 = IntVar(value=1)

cb1 = Checkbutton(
    root,
    image=off_image,
    selectimage=on_image,
    indicatoron=False,
    onvalue=1,
    offvalue=0,
    variable=val1
)

cb2 = Checkbutton(
    root,
    image=off_image,
    selectimage=on_image,
    indicatoron=False,
    onvalue=1,
    offvalue=0,
    variable=val2
)

cb1.pack(padx=10, pady=10)
cb2.pack(padx=10, pady=10)

root.mainloop()
