from itertools import count

import random

pin = random.randint(1111, 9999)  # random liczba od 1-100
print("This is your PIN number:", pin)
count = int(0)
while True and count != 3:
    wpisane_przez_uzytkownika = int(input("Type your PIN: "))
    if wpisane_przez_uzytkownika == pin:
        print("Valid PIN number")
        break
    elif wpisane_przez_uzytkownika != pin:
        print("Invalid PIN number")
        count += 1
        print("Invalid tries:", count)
    if count == 3:
        print("Too many invalid inputs")

logins = ["User1", "User2", "User3", "User4", "User5"]
i = [0, 4]
element1 = []

usernum = print(random.randint(0, 4))


def my_Function():
    print("sus")
    # for i in logins:
    # element1.append(logins[int(wpisany_numer_usera)])
    # print(element1)


wpisany_numer_usera = int(input("Please enter your user number:"))
if wpisany_numer_usera == usernum:
    my_Function()
else:
    print("2")

# passwords = ["password1", "password2", "password3", "password4", "password5"]