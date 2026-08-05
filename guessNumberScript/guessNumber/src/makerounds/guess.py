from random import randrange
import winsound, time

human = 0
computer = 0

abuse = [
    "Is that even a number?!",
    "NO! Wrong",
    "Wrong!",
    "Don't give up now. You can do it",
    "I belive in you!"
    ]

# rando = randrange()
# def forloop(a, b):
#     if a > b:
#         while a >= b:
#             a -= 1
#             print(a)
#     elif a < b:
#         while a <= b:
#             a += 1
#             print(a) 
#     return ""


# print(forloop(2, 10))
# print(forloop(10, 2))

while True:
    try:
        hidden_number = randrange(1, 20)
        guess = int(input("Enter any number from 1 to 20: "))

        if guess == hidden_number and human >= 50:
            winsound.Beep(10000, 500)
            print("Congratulations! You have won this round.\n")
            human += 5
        if guess == hidden_number:
            winsound.Beep(10000, 500)
            print("Congratulations! You have won this round.\n")
            human += 10
            print(f"Human: {human} || Computer: {computer}\n")
            print(f"Human: {human} || Computer: {computer}\n")
        elif (guess < 0):
            winsound.Beep(1000, 500)
            print("Only positive intergers!\n")
            print(f"The hidden number was {hidden_number}")
        elif(guess > 20):
            winsound.Beep(1000, 500)
            print("Number exceeded the limit\n")
            print(f"The hidden number was {hidden_number}")
        elif (guess < hidden_number):
            winsound.Beep(1000, 500)
            print("OOO! So close! \nTry again.")
            computer += 1
            print(f"Human: {human} || Computer: {computer}\n")
            print(f"The hidden number was {hidden_number}")
        elif (guess > hidden_number):
            winsound.Beep(1000, 500)
            print("OOO!! So close! \nTry again.")
            computer += 1
            print(f"Human: {human} || Computer: {computer}\n")
            print(f"The hidden number was {hidden_number}")
    except ValueError:
        winsound.Beep(1000, 500)
        print("Only intergers are valid!\n")
        print(f"The hidden number was {hidden_number}")

    state = input("Enter 'End' to exit the game.\n")
    if state.lower() == 'end':
        print("Exiting code...")
        time.sleep(5)
        break
# (hidden_number + 5 < 60) and      (hidden_number -5 > 0) and 