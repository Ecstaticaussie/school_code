from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton
"""
Need the user to input the number of terms - integers
Get the starting amount -> A float to 2d.p.
Get the annual interest rate from the user -> get a percentage and make it a float based on years
Calculate the time for the user to pay the loan back -> Do it in terms of years
"""

def calc_mortgage(event):
    starting_amount = float(starting_amount_entry.get())
    interest_rate = annual_interest_entry.get() / 12
    terms = int(terms_entry.get()) * 12

    monthly_payment = starting_amount * (interest_rate*(1 + interest_rate)**terms/((1 + interest_rate)**terms)-1)

#The info about the window 
root = CTk()
root.title("Mortgage calculator")
root.geometry("340x400")

starting_amount_label = CTkLabel(root, text="Starting Amount")
starting_amount_label.place(x=20, y=10)

starting_amount_entry = CTkEntry(root)
starting_amount_entry.place(x=130, y=10)

annual_interest_label = CTkLabel(root, text="Annual_interest")
annual_interest_label.place(x=20, y=50)

annual_interest_entry = CTkEntry(root, placeholder_text="Give as a Percentage %")
annual_interest_entry.place(x=130, y=50)

terms_label = CTkLabel(root, text="Number of Terms")
terms_label.place(x=20, y=90)

terms_entry = CTkEntry(root, placeholder_text="Give it in Years")
terms_entry.place(x=130, y=90)

calc_button = CTkButton(root, text="Calculate Mortgage Time", command=calc_mortgage)
calc_button.place(x=65, y=140)
root.mainloop()