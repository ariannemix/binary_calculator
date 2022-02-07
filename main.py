from UserInt import User

print("**Binary Calculator**")
ui = User()
while ui.open == True:

    print(f"\n{'-' * 50}\n"
          "(B)inary to Decimal Conversion\n"
          "(D)ecimal to Binary Conversion\n"
          "(A)dd two binary numbers\n"
          "(S)ubtract two binary numbers\n"
          "(M)ultiply two binary numbers\n"
          "D(i)vide two binary numbers\n"
          "(Q)uit")
    user_input = input('')

    if user_input.upper() == 'B':
        ui.binary()

    if user_input.upper() == 'D':
        ui.decimal()

    if user_input.upper() == 'A':
        ui.add()

    if user_input.upper() == 'S':
        ui.subtract()

    if user_input.upper() == 'M':
        ui.multiply()

    if user_input.lower() == 'i':
        ui.divide()

    if user_input.upper() == 'Q':
        ui.quit()

    if user_input.upper() != 'Q':
        cont = input("Press <enter> to continue. ")
        if cont == '':
            continue
        else:
            break
