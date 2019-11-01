# Program that produces 2 integers, root and pwr, such that 1 < pwr < 6 and root**pwr is equal to the integer entered by the user

user_number = int(input("Enter an Integer: "))
ans = 0
root = 1
while root <= user_number:
    for pwr in range(2, 6):
        ans = root ** pwr
        if ans == user_number:
            break
    if ans == user_number:
        print("root: " + str(root) + " pwr: " + str(pwr))
        break
    else:
        root += 1
if ans != user_number:
    print("It doesn't exist")


