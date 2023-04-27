from tkinter import Tk, StringVar
from tkinter.ttk import Label, Button, Entry
import matplotlib.pyplot as plt

#Information about the window - Name, size, resisability
root = Tk()
root.title("Triangle Checker")
root.geometry("340x300")

#this is to close and open the graph again
is_graph_open = False

#Draw the traingle if valid on a graph
def draw_triangle(side1, side2, side3):
    #This is for the first side
    x1 = [0, side1]
    y1 = [0, 0]

    #This is for working out the top most vertex of the triangle
    
    """
    equation of circle with r = side2: x**2 + y**2 = side2**2
    y**2 = side2**2 - x**2
    y = (side2**2 - x**2)**0.5

    equation of circle with r = side3: (x-side1)**2 + y**2 = side3**2
    y**2 = side3**2 - (x-side1)**2

    Make the equations equal to each other and solve for x:
    side2**2 - x**2 = side3**2 - (x-side1)**2
    side2**2 - x**2 = side3**2 - x**2 - 2*side1*x + side1**2
    side2**2 = side3**2 - 2*side1*x + side1**2
    2*side1*x = side3**2 + side1**2 - side2**2
    x = (side3**2 + side1**2 - side2**2) / side1*2

    Sub this x value into y = (side2**2 - x**2)**0.5 to get the y value

    (x, y) are the coordinates for the topmost vertex
    """

    topmost_x = (side3**2 + side1**2 - side2**2) / side1*2
    topmost_y = (side2**2 - topmost_x**2)**0.5


    #This is for the second side
    x2 = [0, topmost_x]
    y2 = [0, topmost_y]

    #This is for the third side
    x3 = [side1, topmost_x]
    y3 = [0, topmost_y]

    #Giving values for the axis
    plt.xticks([i for i in range(side1+1)])
    plt.yticks([i - 2 for i in range(22)])

    #Checking to see if a graph is already drawn
    if is_graph_open:
        plt.close()
    else: is_graph_open = True
    plt.plot(x1, y1)
    plt.plot(x1, y1)
    plt.plot(x1, y1)
    plt.show()

#Used to show messages easier
def show_message(txt):
    global message_label
    message_label.destroy()
    message_label = Label(root, text=txt)
    message_label.grid(row=5, column=1)

#This is done to check if the inputs and sides are correct
def check_sides(event):
    #Checks to see if all entry boxes have an input
    if (side1_entry.get() == "" or side2_entry.get() == "" or side3_entry.get() == ""):
        show_message("All entry boxes need to be filled.")
    #Checks to see if the entry boxes has any 0's
    elif (side1_entry.get() == "0" or side2_entry.get() == "0" or side3_entry.get() == "0"):
        show_message("Don't input 0's.")
    #Checks to see if the inputs are integers (tried to make it using a minimal amount of lines)
    elif not(side1_entry.get().isdigit() and side2_entry.get().isdigit() and side3_entry.get().isdigit()):
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
        if sum(sides) >= longest_side:
            show_message("This triangle is valid.")
            draw_triangle(side1, side2, side3)
        else: show_message("This triangle is invalid.")

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

#This is done to replace the message shown underneath the check button
message_label = Label(root, text=" ")
message_label.grid(row=5, column=1)

root.mainloop()