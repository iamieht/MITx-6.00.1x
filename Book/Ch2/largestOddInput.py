# Ask for 10 numbers and print the largest odd that was entered

numbers = []
user_input = input("Enter 10 numbers separated by commas: ")
numbers = user_input.split(',')
odds = []
for num in numbers:
    if int(num)%2 != 0:
        odds.append(num)

print(max(odds))
