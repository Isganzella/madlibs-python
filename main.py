import storys

print("**********************************")
print("        WELCOME TO MADLIBS        ")
print("**********************************")
print("**********CHOSE A STORY***********")
print("* 1 => CHIKEN                    *")
print("* 2 => VACUUM                    *")
print("* 3 => LOVE                      *")
print("* 4 => HOT DOG                   *")
print("* 5 => GO OUT                    *")
print("**********************************")

game = True

while game:
    print()
    option = int(input("What's your choice? "))
    if option == 1:
        storys.chiken()
    elif option == 2:
        storys.vacuum()
    elif option == 3:
        storys.love()
    elif option == 4:
        storys.hot_dog()
    elif option == 5:
        print("End of the game")
        break
    else:
        print("Invalid option!!")
        continue





