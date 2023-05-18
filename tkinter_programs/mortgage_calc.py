from customtkinter import CTk, CTkLabel

"""
Need the user to input the number of terms - integers
Get the starting amount -> A float to 2d.p.
Get the annual interest rate from the user -> get a percentage and make it a float based on the regular intervals
Calculate the time for the user to pay the loan back -> Do it in terms of the regular intervals

Extension:
Allow user to change the interval (e.g. monthly)
"""

#Where the root class is made
class Root(CTk):
    def __init__(self):
        super().__init__()

        #Window information
        self.title("Mortgage Calculator ")
        self.geometry("400x400")

        #Entry box to allow the user to choose the regular interval
root = Root()
root.mainloop()