from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("After school routine checker")
window.geometry("600x700")
def check_task():
    task=entry.get()
    if task=="":
        messagebox.showwarning("Warning","No task entered!")
    else:
        lbl=Label(window,text="Next task: "+task)
        lbl.pack()
def show_last_char(event):
    task=entry.get()
    if task!="":
        lbl=Label(window,text="Last character: "+task[-1])
        lbl.pack()
entry=Entry(window)
btn=Button(window,text="Check",command=check_task)
entry.pack()
btn.pack()
entry.bind("<KeyRelease>",show_last_char)
window.mainloop()