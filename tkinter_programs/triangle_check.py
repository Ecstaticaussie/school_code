from tkinter import Tk, StringVar
from tkinter.ttk import Label, Button, Entry

def check_sides(event):
    print("Check")

#Used tp keep the inputs of the entry boxes
side1_txt = StringVar()
side1_txt = StringVar()
side1_txt = StringVar()
#Information about the window - Name, size, resisability
root = Tk()
root.title("Triangle Checker")
root.geometry("500x300")
root.resizable(False, False)

#Introduction message at the top
intro_label = Label(root, text="Enter sides to check if they make a triangle:")
intro_label.pack()

#Labels for each entry box
side1_label = Label(root, text="Side 1:")
side1_label.pack()

side1_label = Label(root, text="Side 2:")
side1_label.pack()

side1_label = Label(root, text="Side 3:")
side1_label.pack()

#Entry boxes to enter the 3 sides
entry1 = Entry(root)
entry1.pack()

entry2 = Entry(root)
entry2.pack()

entry3 = Entry(root)
entry3.pack()

#A button to check if the sides make a triangle
check_button = Button(root, text="Check")
check_button.bind("<Button-1>", check_sides)
check_button.focus()
check_button.pack()
root.mainloop()