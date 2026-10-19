password = list(input("введите пароль\n"))

up_letter = False
down_letter = False
have_digit = False
have_symbol = False

if len(password) == 8 :
    for char in password:
        if char.isupper():
            up_letter = True

        if char.islower():
            down_letter = True
          
        if char.isdigit():
            have_digit = True
               
        if char in "*-#":
            have_symbol = True
        
    if up_letter == False :
        print("в пароле нет заглавных букв")
    elif down_letter == False :
        print("в пароле нет строчных букв")
    elif have_digit == False :
        print("в пароле нет цифр")
    elif have_symbol == False :
        print("в пароле нет специальных символов")
    else:
        print("надежный пароль")
else:
    print("Длина пароля не равна 8")
    