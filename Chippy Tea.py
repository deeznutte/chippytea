#importing stuff
import time
import os
import sys
from playsound import playsound
from PIL import Image
im = Image.open('image.jpg') # opening an image
#set a ton of variables needed later
fishchips = 5.00
sausage = 1.80
pie = 2.00
drinks = 0.80
main = 0.00
order = 0.00
# more import
from hashlib import md5
from getpass import getpass
import sys
def sussy(): #first def
    global sussy
    def order(): #do nested defs work?
        global main #need this otherwise error
        mainin=input(print("Choose a food - Fish and Chips, Pie (P), Jumbo sausage (S)\n")) #first order
        if mainin=="P" or mainin=="p" or mainin=="pie" or mainin=="Pie":
            main=main+2.00
        elif mainin=="S" or mainin=="s":
            main=main+1.80
        elif mainin=="FC" or mainin=="fc":
            main=main+5.00
        else:
            print("Sorry, response not understood")
            playsound("error.mp3")
            exit() #exits if answer not detected (proabably not a good system)
        dnkchc=input(print("Would you like a drink?")) # you can add a drink
        if dnkchc == "y" or dnkchc == "Y":
            dnkcnt=int(input(print("How many drinks?"))) # multiple drinks
            drincc = input(print("Choose a drink\n"))
            tmp=drinks*float(dnkcnt)
            order+=tmp
        ans=input(print("Would you like to add gravy for £1? (Y/N)\n")) #optional
        if ans=="Y":
            order+=1.00
        else:
            print("OK")
        order+=main
        if order >= 25.00: #limited budget
            print("No more money")
            playsound("error.mp3")
            exit()
        print("That will be £" + str(float(order))) #make everything printable
        print("Thank you for ordering w/ Chippy Tea powered by Renault")
        print("Your order will take 30 mins, here is some music while you wait")
        playsound('music.mp3')
        im.show() #show that image done earlier
    #the menu
    print ("Welcome to the Chippy Tea!")
    print ("Option 1 - Place Order")           
    print ("Option 2 - Show Chippy Details")
    print ("Option 3 - Exit")
    print ("Type the number of the option")
    option=int(input())
    if option == 1:
        order()
    elif option == 2:
        print ("Local Chips")
        print ("11 Chips way")
        print ("07484 664409")
    elif option == 3:
        print ("Thank you for ordering with us today")
        print ("We hope to see you soon")
        print("This program will close")
        time.sleep(3)
        exit()
    else:
        print("SUSTEM ERROR")
        playsound("error.mp3")
print("Chippy Tea Login")
#the rest of it manages login, no idea if it works
attempts = 0
check_username = "fb81876b034ee0cb7ead60863baf50d3" # deez in md5
check_password = "ada7ccc63c2b3beb23f89e9243c52a1e" # nyaaaaa but in md5
while True: 
    username = input("Username: ")
    password = getpass("Password: ")
    # Getpass will not echo input to the screen, so your password remains invisible
    print()
    if attempts == 3:
        sys.exit("Too many failed attempts.")
    if md5(username.encode()).hexdigest() == check_username:
        if md5(password.encode()).hexdigest() == check_password: 
            print("Welcome")
            sussy() #call the main function
               
            # Username and password match - do something here
        else:
            print("Password entered incorrectly.")
            attempts += 1
    else:
        print("Username entered incorrectly.")
        attempts += 1
