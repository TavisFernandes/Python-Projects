from random import randint

n = int(input("Enter how many dice you want to roll: "))
count = 1
for i in range(n):
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    choice = input("Roll a dice(y/n): ").lower()
    if i == n-1:
        print("Thank you for playing!")
    elif choice == "y":
        print(f"({die1},{die2})")
        count += i
    elif choice == "n":
        print("Thank you for playing!")
        break
    else:
        print("Invalid input")
print(f"You rolled {count} dice out of {n}.")