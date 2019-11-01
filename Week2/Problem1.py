# Problem 1 - Paying Debt off in a Year 

# Test Case 1:
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Variables
monthlyInterestRate = annualInterestRate / 12.0

# Program Logic
for month in range(1, 13):
    minMonthlyPayment = monthlyPaymentRate * balance
    unpaidBalance = balance - minMonthlyPayment
    balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)

print("Remaining balance:", round(balance, 2))







