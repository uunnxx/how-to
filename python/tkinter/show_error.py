from tkinter import (
    Tk,
    Button,
    messagebox
)


root = Tk()
root.geometry('300x150')
root.title('Error Message')


def display():
    messagebox.showerror(
        'Show Error Example', 'This is a basic error message example'
    )

btn = Button(root, text='Click Error Message', command=display)
btn.pack()
root.mainloop()
