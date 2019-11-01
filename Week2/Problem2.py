# Problem 2 - Paying Debt Off in a Year 

#Test Case 1:
balance = 3926
annualInterestRate = 0.2

# Variables
minFixedMonthlyPayment = 10
monthlyInterestRate = annualInterestRate / 12.0
updatedBalance = balance

while True:
    for month in range(1,13):
        monthlyUnpaidBalance = updatedBalance - minFixedMonthlyPayment
        updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

    if updatedBalance > 0:
        minFixedMonthlyPayment += 10
        updatedBalance = balance
    else:
        print("Lowest Payment:", minFixedMonthlyPayment)
        break


