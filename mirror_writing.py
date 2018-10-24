#import modules
import time

print("")
print("Welcome to the...")
time.sleep(1)
print("*************************************************************************")
time.sleep(0.3)
print("* __    __     __     ______     ______     ______     ______           *")
time.sleep(0.3)
print("*/\ '-./  \   /\ \   /\  == \   /\  == \   /\  __ \   /\  == \          *")
time.sleep(0.3)
print("*\ \ \-./\ \  \ \ \  \ \  __<   \ \  __<   \ \ \/\ \  \ \  __<          *")
time.sleep(0.3)
print("* \ \_\ \ \_\  \ \_\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\        *")
time.sleep(0.3)
print("*  \/_/  \/_/   \/_/   \/_/ /_/   \/_/ /_/   \/_____/   \/_/ /_/        *")
time.sleep(0.3)
print("*                                                                       *")
time.sleep(0.3)
print("* __     __     ______     __     ______   __     __   __     ______    *")
time.sleep(0.3)
print("*/\ \  _ \ \   /\  == \   /\ \   /\__  _\ /\ \   /\ '-.\ \   /\  ___\   *")
time.sleep(0.3)
print("*\ \ \/ '.\ \  \ \  __<   \ \ \  \/_/\ \/ \ \ \  \ \ \-.  \  \ \ \__ \  *")
time.sleep(0.3)
print("* \ \__/'.~\_\  \ \_\ \_\  \ \_\    \ \_\  \ \_\  \ \_\\'\_\  \ \_____\ *")
time.sleep(0.3)
print("*  \/_/   \/_/   \/_/ /_/   \/_/     \/_/   \/_/   \/_/ \/_/   \/_____/ *")
time.sleep(0.3)
print("*                                                                       *")
time.sleep(0.3)
print("*          ______     __     ______   __  __     ______     ______      *")
time.sleep(0.3)
print("*         /\  ___\   /\ \   /\  == \ /\ \_\ \   /\  ___\   /\  == \     *")
time.sleep(0.3)
print("*         \ \ \____  \ \ \  \ \  _-/ \ \  __ \  \ \  __\   \ \  __<     *")
time.sleep(0.3)
print("*          \ \_____\  \ \_\  \ \_\    \ \_\ \_\  \ \_____\  \ \_\ \_\   *")
time.sleep(0.3)
print("*           \/_____/   \/_/   \/_/     \/_/\/_/   \/_____/   \/_/ /_/   *")
time.sleep(0.3)
print("*                                                                       *")
time.sleep(0.3)
print("*************************************************************************")
time.sleep(0.5)
print("")
input("Press enter to continue.")

while True:

    print("")
    clear_text = input("What is your message? ")
    cipher_text = clear_text[::-1]

    print(cipher_text)
    
    menu_choice = input("Would you like to decrypt your message? Yes or No?")
    
    
    if menu_choice == "Yes" or menu_choice == "yes":
        print("The decrypted message is:", clear_text)
    
        menu_choice2 = input("Would you like to try again? Yes or No?")
        
        if menu_choice2 == "Yes" or menu_choice == "yes":
            clear_text = input("What is your message? ")
            cipher_text = clear_text[::-1]
            
            print(cipher_text)
    
            menu_choice = input("Would you like to decrypt your message? Yes or No?")
    
    
            if menu_choice == "Yes" or menu_choice == "yes":
                print("The decrypted mesage is:", clear_text)
                break

            else:
                break

        else:
            break
    else:
        menu_choice2 = input("Would you like to try again? Yes or No?")
        
        if menu_choice2 == "Yes" or menu_choice == "yes":
            clear_text = input("What is your message? ")
            cipher_text = clear_text[::-1]

            print(cipher_text)
    
            menu_choice = input("Would you like to decrypt your message? Yes or No?")
    
    
            if menu_choice == "Yes" or menu_choice =="yes":
                print("The decrypted mesage is:", clear_text)
    
        else:
            break
    
print("Goodbye.")
