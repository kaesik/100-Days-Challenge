year = int(input("Which year do you want to check?\n"))
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("przestępny")
        else:
            print("nieprzestępny")
    else:
        print("przestępny")
else:
    print("nieprzestępny")
 