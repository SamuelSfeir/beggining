while True:
    user_input = input("Type a number to divide by two or write 'out' to get out: ")
    if user_input == "out" or user_input == "Out" or user_input == "OUT":
        print("Gotcha! Taking you out")
        break
    number = int(user_input)
    print('There you go:',number/2)
