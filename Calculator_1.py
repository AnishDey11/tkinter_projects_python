from tkinter import *
from tkinter import StringVar


def add_element(element: str):
    curr = eqnvar.get()
    updated = curr + element
    eqnvar.set(updated)


def solve():
    equation = eqnvar.get()
    eqnvar.set(eval(equation))


def clean():
    after_clean = eqnvar.get()[0:-1]
    eqnvar.set(after_clean)


def clear_all():
    eqnvar.set('')


window = Tk()

icon_img = PhotoImage(file='img.png')

window.geometry('346x500')
window.resizable(False, False)
window.title('Calculator')
window.iconphoto(True, icon_img)

button_frame = Frame(window, bg='grey', height='372', width='346')
button_frame.pack_propagate(False)
button_frame.pack(side=BOTTOM, pady=5, padx=5)

Button(button_frame, width=10, height=4, pady=2, padx=2, text='(', command=lambda: add_element('(')).place(x=0, y=0)
Button(button_frame, width=10, height=4, pady=2, padx=2, text=')', command=lambda: add_element(')')).place(x=85, y=0)
Button(button_frame, width=10, height=4, pady=2, padx=2, text='C', command=clean).place(x=170, y=0)
Button(button_frame, width=10, height=4, pady=2, padx=2, text='➗', command=lambda: add_element('/')).place(x=255, y=0)

Button(button_frame, width=10, height=4, pady=2, padx=2, text='7', command=lambda: add_element('7')).place(x=0, y=75)
Button(button_frame, width=10, height=4, pady=2, padx=2, text='8', command=lambda: add_element('8')).place(x=85, y=75)
Button(button_frame, width=10, height=4, pady=2, padx=2, text='9', command=lambda: add_element('9')).place(x=170, y=75)
Button(button_frame, width=10, height=4, pady=2, padx=2, text='✖️', command=lambda: add_element('*')).place(x=255, y=75)

Button(button_frame, width=10, height=4, pady=2, padx=2, text='4', command=lambda: add_element('4')).place(x=0, y=150)
Button(button_frame, width=10, height=4, pady=2, padx=2, text='5', command=lambda: add_element('5')).place(x=85, y=150)
Button(button_frame, width=10, height=4, pady=2, padx=2, text='6', command=lambda: add_element('6')).place(x=170, y=150)
Button(button_frame, width=10, height=4, pady=2, padx=2, text='➖', command=lambda: add_element('-')).place(x=255, y=150)

Button(button_frame, width=10, height=4, pady=2, padx=2, text='1', command=lambda: add_element('1')).place(x=0, y=225)
Button(button_frame, width=10, height=4, pady=2, padx=2, text='2', command=lambda: add_element('2')).place(x=85, y=225)
Button(button_frame, width=10, height=4, pady=2, padx=2, text='3', command=lambda: add_element('3')).place(x=170, y=225)
Button(button_frame, width=10, height=4, pady=2, padx=2, text='➕', command=lambda: add_element('+')).place(x=255, y=225)

Button(button_frame, width=10, height=4, pady=2, padx=2, text='CA', command=clear_all).place(x=0, y=300)
Button(button_frame, width=10, height=4, pady=2, padx=2, text='0', command=lambda: add_element('0')).place(x=85, y=300)
Button(button_frame, width=10, height=4, pady=2, padx=2, text='.', command=lambda: add_element('.')).place(x=170, y=300)
Button(button_frame, width=10, height=4, pady=2, padx=2, text='🟰', command=solve).place(x=255, y=300)

result_frame = Frame(window, height='120', width='346')
result_frame.pack_propagate(False)
result_frame.pack(side=TOP, padx=5, pady=5)

eqnvar = StringVar()

equation_label = Label(result_frame, textvariable=eqnvar, font=('Arial', 20), anchor='se', bg='lightgrey')
equation_label.pack(fill='both', expand=True)

window.mainloop()
