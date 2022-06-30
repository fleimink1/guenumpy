import random
from pyfiglet import Figlet

r1 = random.randint(1,100)
preview_text = Figlet(font='slant')
print(preview_text.renderText('GUENUMPY'))
name = input("NickName: ")

attempts = 0

while attempts < 26:
    print("used attempts: " + str(attempts))
    a = int(input("Guess the number: "))

    attempts += 1

    if a < r1:
        print("More")
        
    elif a > r1:
        print("Less")
        
    elif a == r1:
        break

if a == r1:
    print("You Win. Recorded in result.txt")
    file = open("result.txt", "a")
    file.write(f"Name: {name}, how did you guess: {attempts}, Guessed the number: {r1}\n")
    file.close
else:
    print("You lose :(")