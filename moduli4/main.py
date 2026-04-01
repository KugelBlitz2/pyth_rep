def greet(by, byu):
    return by + byu

print(greet(5, 6))

def greet_person(name):
    print("Hello", name)

greet_person("Test")

def tryvrb(name):
    global messages
    messages = f"Hello, {name}"
    print(messages)

tryvrb("Testim")

greeting = "Hello"

def hello(greety):
    messages = f"Hello, {greety}"
    print(messages)

hello("Ylli")

print(greeting)

def greet_meaning(name, greetings="Hello"):
    messagesi = f"{greetings} {name}"
    return messagesi

print(greet_meaning("Alice"))

suny = 0

for numb in range(1, 11):
        if numb % 2 == 0:
            suny += numb


print(suny)