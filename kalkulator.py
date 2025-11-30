wybor = ""
def menu():
    while True:
        print("======== KALKULATOR ========")
        print("1. dodawanie")
        print("2. odejmowanie")
        print("3. mnożenie")
        print("4. dzielenie")
        print("5. wyjście")
        print("===========================")

        wybor = input("Wybierz operację (1-5): ")

        if wybor == "5":
            print("Koniec programu.")
            break
        if wybor == "1":
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))
            print(f"Wynik: {a} + {b} = {a + b}")
        elif wybor == "2":
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))
            print(f"Wynik: {a} - {b} = {a - b}")
        elif wybor == "3":
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))
            print(f"Wynik: {a} * {b} = {a * b}")
        elif wybor == "4":
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))
            if b != 0:
                print(f"Wynik: {a} / {b} = {a / b}")
            else:
                print("Błąd: Nie można dzielić przez zero.")


        
menu()