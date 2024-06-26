from tkinter import *
from tkinter import filedialog


def openfile():
    file_path = filedialog.askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*')])
    if file_path:
        with open(file_path, 'r') as file:
            text_entry.delete(1.0, END)
            text_entry.insert(END, file.read())


def savefile():
    file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[('Text Files', '*.txt'),
                                                                        ('All Files', '*.*')])
    file_text = str(text_entry.get(1.0, END))
    file.write(file_text)
    file.close()


window = Tk()
window.geometry('1000x650')
window.title("Text Editor")

menubar = Menu(window)
window.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=openfile)
file_menu.add_command(label='Save', command=savefile)
file_menu.add_command(label='Exit', command=quit)

text_entry = Text(window, font=('arial', '15'))
text_entry.pack(fill='both', expand=True)

window.mainloop()
