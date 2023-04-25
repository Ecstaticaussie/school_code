from tkinter import Tk
from tkinter.ttk import Label, Button

def check_sides(side1, side2, side3):
    print("Check")
    
#Information about the window - Name, size, resisability
root = Tk()
root.title("Triangle Checker")
root.geometry("500x300")
root.resizable(False, False)

#Introduction message at the top
intro_label = Label(root, text="Enter sides to check if they make a triangle:")
intro_label.pack()

#A button to check if the sides make a triangle
check_button = Button(root, text="Check", command=check_sides(1, 2, 3))
check_button.pack()
root.mainloop()