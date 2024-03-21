import random

top_of_range= input("Enter a number for the range: ")
guesses=0

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("Please enter a number greaten than zero next time!")
else:
    print("Please enter valid characters")
    
random_number = random.randint(0, top_of_range)  

while True:
    number_entered_byuser= input("Guess the number: ")
    guesses += 1

    if number_entered_byuser.isdigit():
        number_entered_byuser=int(number_entered_byuser)
        if number_entered_byuser <=0:
            print("Please enter a number greaten than zero next time!")
            break
    else:
        print("Please enter valid characters")
        break
    
    if number_entered_byuser==random_number:
        print("You got it on the {0}th try".format(guesses))
        break
    else:
        print("you got it wrong")
        if number_entered_byuser>random_number:
            print("try a smaller number")
        elif number_entered_byuser<random_number:
            print("Try a larger number")

    
    