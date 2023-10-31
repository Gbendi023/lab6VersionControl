# this is my first git hub experiement
#list(str(94879599)) = [9,4,8,.......]

prog = True

while prog:
    print('would you like to encode or decode a password? ', end='')
    option = str(input(""))


    if option == "encode":
        print("Please enter your eight digit password: ", end='')
        elist = int(input(""))

        if elist< 0:
            print("Incorrect password format. Try again!")
            continue

        print(f"your encoded value is: {elist+33333333}")
        continue

    if option == "decode":
        print("Please enter your eight digit password: ", end='')
        dlist = int(input(""))

        if dlist< 0:
            print("Incorrect password format. Try again!")
            continue

        print(f"your encoded value is: {dlist-33333333}")
        continue
