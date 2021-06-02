import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

win = tk.Tk()
#window Title
win.title("Ad Click Fraud detection")
#Window size
win.geometry("1200x800")
#window background color
#win.config(background="white")
#select dataset label
l1=Label(win,text="Uploading dataset:",font=("Arial",15))

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("Text files",
                                                      "*.txt*"),("all files","*.*")))
    messagebox.showinfo("Message","Selected file name is " +filename)
    messagebox.showinfo("Message", "Dataset Uploaded successfully")
    tb2.insert(END,"selected file name is: "+filename+"\n")
    tb2.insert(END, "Dataset Uploaded successfully \n")


label_file_explorer = Label(win,text="Select a File")
tb1=Text(win, height=1,width=20)
tb1.insert(END,"file path")
b1 = Button(win,text="Browse",command=browseFiles,font=("Arial",12))
l1.grid(row=0, column=0)
label_file_explorer.grid(row=1, column=0)
tb1.grid(row=1, column=1)
b1.grid(row=1, column=2)
l2=Label(win,text="select Algorithm", font=("Arial",12))
l2.grid(row=2, column=0)

var = tk.StringVar()
def print_selection():
    tb2.insert(END,"selected Algorithm is: " + var.get()+"\n")
r1 = tk.Radiobutton(win, text='Logistic Regression', variable=var, value='Logistic Regression', command=print_selection,font=("Arial",12))
r1.grid(row=3, column=0)
r2 = tk.Radiobutton(win, text='Support Vector Machine', variable=var, value='Support Vector Machine', command=print_selection,font=("Arial",12))
r2.grid(row=3, column=1)
r3 = tk.Radiobutton(win, text='Deep Neural Network', variable=var, value='Deep Neural Network', command=print_selection,font=("Arial",12))
r3.grid(row=3, column=2)
def applyalgorithm():
    tb2.insert(END,"Algorithm Initiated..........\n")
    tb2.insert(END, "Algorithm Completed........\n")
    tb2.insert(END, "Result displayed........\n")
b2= Button(win,text="Apply Algorithm",command=applyalgorithm,font=("Arial",12))
b2.grid(row=4, column=0)
l3=Label(win,text="OUTPUT:",font=("Arial",15))
l3.grid(row=6, column=0)
tb2=Text(win, height=25,width=100)
tb2.place(x=10,y=200)
win.mainloop()
print("hello")