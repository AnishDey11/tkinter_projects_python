from tkinter import *


# All button functions
def delete_task():
    list_box.delete(list_box.curselection()[0])


def mark_as_read():
    marked_ind = list_box.curselection()[0]
    marked_text = list_box.get(list_box.curselection())
    marked_text = marked_text + ' ✔'
    list_box.delete(marked_ind)
    list_box.insert(marked_ind, marked_text)


def clear_text():
    task_entry.delete(0, END)


def add_task():
    new_task = task_entry.get()
    new_task = '¤  ' + new_task
    list_box.insert(list_box.size(), new_task)
    task_entry.delete(0, END)


window = Tk()

icon_img = PhotoImage(file='icon.png')

window.title("To-Do-List")
window.geometry("860x520")
window.resizable(False, False)
window.iconphoto(True, icon_img)

# All add task and task window here
frame_text = Frame(window, height='520', width='600', bg='pink')
frame_text.pack_propagate(False)
frame_text.pack(side=RIGHT)

# For delete amd mark as read button
frame_work = Frame(window, height='520', width='260', bg='lightblue')
frame_work.pack_propagate(False)
frame_work.pack(side=LEFT)

# A frame only to show task in another frame
new_frame = Frame(frame_text, height='400', width='550')
new_frame.pack_propagate(False)
new_frame.pack(side=BOTTOM, pady=8)

Label(frame_text, text='Your Tasks', bg='pink', font='Arial', pady=5).pack(side=TOP)

Canvas(frame_text, width=550, height=2, bg="blue", bd=0, highlightthickness=0).pack(pady=2)

task_entry = Entry(frame_text, font=('calibre', 15), width=50)
task_entry.pack_propagate(False)
task_entry.pack(side=TOP, pady=5, anchor='nw')

# All buttons
Button(frame_text, text='clear', width=4, font=('Helvetica', 10), command=clear_text).place(x=598, y=44, anchor='ne')

Button(frame_text, text='Add Task', font=('Helvetica', 10), pady=5, padx=5, width=55, command=add_task).pack(side=TOP)

Button(frame_work, text='Mark as Read', font=('Helvetica', 10), pady=5, padx=5, width=20, command=mark_as_read).place(x=45, y=60)

Button(frame_work, text='Delete Task', font=('Helvetica', 10), pady=5, padx=5, width=20, command=delete_task).place(x=45, y=120)

list_box = Listbox(new_frame, font=('Helvetica', 15),)
list_box.pack(fill='both', expand=True)

window.mainloop()
