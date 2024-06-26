from tkinter import *
from time import strftime


def time_get():
    time_string = strftime('%I:%M:%S %p\n%d/%m/%y')
    time_label.config(text=time_string)
    time_label.after(1000, time_get)


window = Tk()
window.title('Digital Clock')

time_label = Label(window, font=('calibri', 50, 'bold'), bg='lightgrey', fg='black')
time_label.pack(anchor='center')

time_get()

window.mainloop()


