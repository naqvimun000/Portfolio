#import modules
import time

print("")
print("Welcome to an informational program about...")
time.sleep(1)
print("\033[1;40;32m*************************************************************************\033[0m")
time.sleep(0.3)
print("\033[1;40;32m* ______     __     ______   __  __     ______     ______     ______    *\033[0m")
time.sleep(0.3)
print("\033[1;40;32m*/\  ___\   /\ \   /\  == \ /\ \_\ \   /\  ___\   /\  == \   /\  ___\   *\033[0m")
time.sleep(0.3)
print("\033[1;40;32m*\ \ \____  \ \ \  \ \  _-/ \ \  __ \  \ \  __\   \ \  __<   \ \___  \  *\033[0m")
time.sleep(0.3)
print("\033[1;40;32m* \ \_____\  \ \_\  \ \_\    \ \_\ \_\  \ \_____\  \ \_\ \_\  \/\_____\ *\033[0m")
time.sleep(0.3)
print("\033[1;40;32m*  \/_____/   \/_/   \/_/     \/_/\/_/   \/_____/   \/_/ /_/   \/_____/ *\033[0m")
time.sleep(0.3)
print("\033[1;40;32m*************************************************************************\033[0m")
time.sleep(0.2)

input("\033[1;5;32mPress enter to continue.\033[0m")
print("")
print("A cipher is a method of transforming a text in order to conceal its meaning. There are many different ciphers, but monoalphabetic ciphers and polyalphabetic ciphers are two of the oldest.")
input("\033[1;5;32mPress enter to continue.\033[0m")
print("")

while True:

    menu_choice = input("Type 1 to learn about monoalphabetic ciphers, or type 2 to learn about polyalphabetic ciphers. To exit, type x. Press enter to finalize your choice.")


    if menu_choice == "1":
        print("")
        print("\033[40;1;32mMonoalphabetic Ciphers\033[0m")
        print("")
        print("Monoalphabetic ciphers scramble up the alphabet and use the same pattern for every scrambled letter. These ciphers are very old and have been used since the rule of Caesar. They are also the easiest to decrypt since they use only one pattern.")
        input("\033[1;5;32mPress enter to continue.\033[0m")
        print("")
        menu_choice2 = input("Would you like an example? Yes or No?")


        if menu_choice2 == "Yes" or menu_choice2 == "yes":
            print("")
            print("An example of a monoalphabetic cipher is the atbash cipher. This cipher flips the alphabet around so that A=Z, B=Y, C=X, and so on.")
            print("")
            clear_text = input("Type in your message:")
            clear_text = clear_text.lower()
            print("")

            input("\033[1;5;32mPress enter to continue\033[0m")
            cipher_text = clear_text.replace("a","Z")
            cipher_text = cipher_text.replace("b","Y")
            cipher_text = cipher_text.replace("c","X")
            cipher_text = cipher_text.replace("d","W")
            cipher_text = cipher_text.replace("e","V")
            cipher_text = cipher_text.replace("f","U")
            cipher_text = cipher_text.replace("g","T")
            cipher_text = cipher_text.replace("h","S")
            cipher_text = cipher_text.replace("i","R")
            cipher_text = cipher_text.replace("j","Q")
            cipher_text = cipher_text.replace("k","P")
            cipher_text = cipher_text.replace("l","O")
            cipher_text = cipher_text.replace("m","N")
            cipher_text = cipher_text.replace("n","M")
            cipher_text = cipher_text.replace("o","L")
            cipher_text = cipher_text.replace("p","K")
            cipher_text = cipher_text.replace("q","J")
            cipher_text = cipher_text.replace("r","I")
            cipher_text = cipher_text.replace("s","H")
            cipher_text = cipher_text.replace("t","G")
            cipher_text = cipher_text.replace("u","F")
            cipher_text = cipher_text.replace("v","E")
            cipher_text = cipher_text.replace("w","D")
            cipher_text = cipher_text.replace("x","C")
            cipher_text = cipher_text.replace("y","B")
            cipher_text = cipher_text.replace("z","A")

            print(cipher_text)

        else: 
            pass

    elif menu_choice == "2":
        print("")
        print("\033[40;1;32mPolyalphabetic Ciphers\033[0m")
        print("")
        print("Polyalphabetic ciphers scramble up the alphabet just like monoalphabetic ciphers, but, unlike monoalphabetic ciphers, they use multiple different patterns to throw off the decrypter. The first polyalphabetic cipher was created in 1467 by Leon Battista Albert. It was called the Vigenere cipher even though it was created 56 years before Vigenere was born.")
        input("\033[1;5;32mPress enter to continue.\033[0m")
        print("")

    elif menu_choice == "x":
        break

    

    else:
        print("")
        print("I'm sorry, I didn't understand you. Please try again.")
        print("")

print("")
print("Goodbye.")
print("")
