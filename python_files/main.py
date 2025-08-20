score = 50
lives = 3
level = 4



print("Hello")
print("Welcome to the program")
name = input("what is your name ")
print("hello", name)
if score >= 50:
    print("You passed!")
else:
    print("Try again.")
for level in range(1, 5):
    print("Level", level)
if lives in range(1, 5):
    print("you not dead")