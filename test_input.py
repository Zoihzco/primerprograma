
number_to_guess = 22

user_number = int(input("adivina un numero: "))

if number_to_guess == user_number:
    print("Has ganado")
else:
    print("Has fallado")
    user_number = int(input("Intentalo de nuevo: "))
    if number_to_guess == user_number:
        print("Has ganado")
    else:
        print("Has fallado , intentalo de nuevo")
        user_number = int(input("adivina un numero: "))
        if number_to_guess == user_number:
            print("Has ganado")
        else:
            print("Has fallado , intentalo de nuevo")
            user_number = int(input("adivina un numero,penultimo intento: "))
            if number_to_guess ==user_number:
                print("Has ganado")
            else:
                print("Has fallado,no tienes mas intento ")
                user_number = int(input("Ultimo intento , adivina numero: "))
                if number_to_guess == user_number:
                    print("Has ganado")
                else:
                    print("Has perdido todos los intentos")