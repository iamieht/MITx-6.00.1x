# Problem 3 - Paying Debt Off in a Year Using Bisection Search to Make the Program Faster

#Test Case 1:
balance = 5000
annualInterestRate = 0.2

# Variables
monthlyInterestRate = annualInterestRate / 12.0
monthlyPaymentLowerBound = round(balance / 12, 2)
monthlyPaymentUpperBound = round((balance * (1 + monthlyInterestRate)**12) / 12.0, 2)
minMonthlyPayment = round((monthlyPaymentUpperBound + monthlyPaymentLowerBound) / 2, 2)
updatedBalance = balance
epsilon = 0.1


while True:
    for month in range(1,13):
         monthlyUnpaidBalance = round(updatedBalance - minMonthlyPayment, 2)
         updatedBalance = round(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance), 2)

    if updatedBalance > 0 and updatedBalance - monthlyUnpaidBalance > epsilon:
        monthlyPaymentLowerBound = minMonthlyPayment
        updatedBalance = balance
    elif updatedBalance < 0 and updatedBalance - monthlyUnpaidBalance < epsilon:
        monthlyPaymentUpperBound = minMonthlyPayment
        updatedBalance = balance
    else:
        print("Lowest Payment:", minMonthlyPayment)
        break
    
    minMonthlyPayment = round((monthlyPaymentUpperBound + monthlyPaymentLowerBound) / 2, 2)



