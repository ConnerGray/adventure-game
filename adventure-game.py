# Author: Conner 
# Date: 1/21/2021

# Intro

name = input("What is your name?" ).lower().strip()
ans = input("hello, " + name + " would you like to go on an adventure? (yes or no)").lower().strip()

# Begining of story
if ans == 'yes':
    print("You wake up in the middle of the night hearing a loud bang outside of your house. ")
    ans = input("Do you investigate the sound or go back to sleep? (sound or sleep)").lower().strip()

    if ans == 'sleep':
        print("You go back to sleep and an intruder enters your home.")

    else:
        print("You go to investigate the sound... You find that it was just your screen door.")    

elif ans == "no":
    print("Fuck you then.") 