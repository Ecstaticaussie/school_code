from tkinter import Tk
from tkinter.ttk import Label, Button, Entry

root = Tk()
root.title("Truth Table v1")
root.geometry("700x400")
def create_table():
    boolean_expression = expression_entry.get().split()
    variables = sorted(list(set([letter for letter in boolean_expression if letter.isalpha()])))

    variable_labels = [Label(root, text=letter) for letter in variables]
    for i in range(len(variable_labels)):
        variable_labels[i].grid(row=0, column=i+1)

    boolean_byte = [bin(num).replace("0b", "") for num in [i for i in range(2**len(variables))]]
    for i in range(len(boolean_byte)):
        while len(boolean_byte[i]) != len(variable_labels):
            boolean_byte[i] = "0" + boolean_byte[i]
    
    boolean_bit_labels = [[Label(root, text=bit) for bit in [*byte_str]] for byte_str in boolean_byte]
    for i in range(len(boolean_bit_labels)):
        for j in range(len(boolean_bit_labels[i])):
            boolean_bit_labels[i][j].grid(row=i+1, column=j+1)

rules_label = Label(root, text="Use single capital letters for the boolean variables and use only the + and * operators")
rules_label.grid(row=0, column=0)
expression_entry = Entry(root, text="Enter Boolean Expression:")
expression_entry.grid(row=1, column=0)
confirm_button = Button(root, text="Create table", command=create_table)
confirm_button.grid(row=2, column=0)

root.mainloop()

#Sorry sir that I didn't make it look better
#There is also the "feature" of not replacing truth tables properly