from random import randint
print("Enter the number range (bigger range for higher difficulty)")
a =int(input("Enter the minimum value: "))
b = int(input("Enter the maximum value: "))
correct_no = randint(a, b)
count = 0
for i in range(3):
    try:
        guess = int(input(f"Guess a number between {a} and {b}: "))
        if guess == correct_no:
            print("Correct!")
            count += 1
            break
        elif guess < correct_no:
            print("To Low!")
            count += 1
        elif guess > correct_no:
            print("To High!")
            count += 1
        if i == 2:
            print("Game Over!")
    except ValueError:
        print("Invalid input!")

print(f"Best Score: {count}")