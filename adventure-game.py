# Author: Conner 
# Date: 1/21/2021

# Intro

name = input("What is your name? " ).lower().strip()
ans = input("hello, " + name + " would you like to go on an adventure? (yes or no) ").lower().strip()

# Begining of story
if ans == 'yes':
    print("\nYou wake up in the middle of the night hearing a loud bang outside of your house. ")
    ans = input("Do you investigate the sound or go back to sleep? (sound or sleep) ").lower().strip()

    if ans == 'sleep':
        print("\nYou try to go back to sleep and an intruder enters your home. You hear him making his way up the stairs. Do you head for your gun or try to lock the door (gun or lock) ")
        ans = input().lower().strip()

        if ans == 'gun':
            print("\nYou make it to your gun and try to shoot the intruder.. but you're out of bullets. He shoots you first. You lost")

        else:
            print("\nYou are able to lock the door. Do you jump out the window or stay and fight? (window or fight)")
            ans = input().lower().strip()

            if ans == 'window':
                print("\nYou jump out of your window and die. You lost")

            else: 
                print("\nYou stay to fight. You grab a bat from your closet and are able to injur the intruder and make it free! You win!")    
    else:
        print("\nYou go to investigate the sound... You find that it was just your screen door.")    

elif ans == "no":
    print("That's too bad.") 