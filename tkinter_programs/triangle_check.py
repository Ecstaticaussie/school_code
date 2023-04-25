from tkinter import Tk, StringVar
from tkinter.ttk import Label, Button, Entry

def show_message(txt):
    message_label = Label(root, text=txt)
    message_label.grid(row=5, column=1)

#This is done to check if the inputs and sides are correct
def check_sides(event):
    #Checks to see if the inputs are integers (tried to make it using a minimal amount of lines)
    if not(side1_entry.get().isdigit() and side2_entry.get().isdigit() and side3_entry.get().isdigit()):
        show_message("Only input INTEGERS!!")
    else:
        #All the values of each side
        side1 = int(side1_entry.get())
        side2 = int(side2_entry.get())
        side3 = int(side3_entry.get())

        #Put into a list for simple evaluation using triangular inequality
        sides = [side1, side2, side3]
        longest_side = max(sides)
        sides.remove(longest_side)

        #Triangular inequality: sum of shorter sides >= longest side
        if sum(sides) >= longest_side: show_message("This triangle is valid")
        else: show_message("This triangle is invalid")

#Information about the window - Name, size, resisability
root = Tk()
root.title("Triangle Checker")
root.geometry("500x300")

#Introduction message at the top
intro_label = Label(root, text="Enter sides to check if they make a triangle :")
intro_label.grid(row=0, column=1)

#Labels for each entry box
side1_label = Label(root, text="  Side 1:")
side1_label.grid(row=1, column=0)

side2_label = Label(root, text="  Side 2:")
side2_label.grid(row=2, column=0)

side3_label = Label(root, text="  Side 3:")
side3_label.grid(row=3, column=0)

#Used tp keep the inputs of the entry boxes
side1_txt = StringVar()
side2_txt = StringVar()
side3_txt = StringVar()

#Entry boxes to enter the 3 sides
side1_entry = Entry(root, textvariable=side1_txt)
side1_entry.grid(row=1, column=1)

side2_entry = Entry(root, textvariable=side2_txt)
side2_entry.grid(row=2, column=1)

side3_entry = Entry(root, textvariable=side3_txt)
side3_entry.grid(row=3, column=1)

#A button to check if the sides make a triangle
check_button = Button(root, text="Check")
check_button.bind("<Button-1>", check_sides)
check_button.focus()
check_button.grid(row=4, column=1)
root.mainloop()