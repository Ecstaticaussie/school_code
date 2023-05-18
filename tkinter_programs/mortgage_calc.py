from customtkinter import CTk, CTkLabel, CTkEntry
"""
Need the user to input the number of terms - integers
Get the starting amount -> A float to 2d.p.
Get the annual interest rate from the user -> get a percentage and make it a float based on years
Calculate the time for the user to pay the loan back -> Do it in terms of years
"""

#The info about the window 
root = CTk()
root.title("Mortgage calculator")
root.geometry("400x400")

starting_amount_label = CTkLabel(root, text="Starting Amount")
starting_amount_label.place(x=20, y=10)

starting_amount_entry = CTkEntry(root)
starting_amount_entry.place(x=130, y=10)

annual_interest_label = CTkLabel(root, text="Annual_interest")
annual_interest_label.place(x=20, y=50)

annual_interest_entry = CTkEntry(root, placeholder_text="Give as a Percentage %")
annual_interest_entry.place(x=130, y=50)

terms_label = CTkLabel(root, text="Starting Amount")
terms_label.place(x=20, y=90)

terms_entry = CTkEntry(root, placeholder_text="Give it in Years")
terms_entry.place(x=130, y=90)

root.mainloop()