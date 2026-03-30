names = ["Test", "Blablabla", "Issac"]

for name in names:
    print(name)

sentence = "Hello World"

for char in sentence:
    if char.isalpha():
        print(char)

for num in range(1, 6):
    print(num)

numbers = [1, 2, 3, 4]

maxi = numbers[0]

for num in numbers:
    if num > maxi:
        maxi = num

print(f"The max is", maxi)

count = 1

while count <= 5:
    print(count)
    count += 1

numbers = [1,2,3,4,5,6]

trg=4

for num in numbers:
    print(num)
    if num == trg:
        print("Target found")
        break

scores = [60,42,57,78,35,62,60,92]

total = 0

count = 0

for score in scores:
    if score < 50:
        total += score
        count += 1

avg = total / count if count > 0 else 0

print(avg)

while True:
    user_input = input("Enter positive number: ")
    if user_input.isnumeric():
        number = int(user_input)

        if number > 0:
            break
        print("Invalid number")

print("You entered a positive number", number)