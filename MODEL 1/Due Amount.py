
total_bill = 275 #input((int)"Please enter your total bill":)
amount_paid = 227 #input((int)"Please enter the amount you paid":)
        
if total_bill < 0 or amount_paid < 0:
    print("Error:Invalid Input.")
else:
    Due_Amount = total_bill - amount_paid
    print("The Due Amount is",Due_Amount )
        
