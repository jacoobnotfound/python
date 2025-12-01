import os
import subprocess

def open_program(program_path):
    try:
        subprocess.Popen(program_path)
        print(f"✓ Otwieranie programu: {program_path}")
    except FileNotFoundError:
        print(f"✗ Nie znaleziono programu: {program_path}")
    except Exception as e:
        print(f"✗ Błąd: {e}")

def menu():
    while True:
        print("\n======== MENU PROGRAMÓW ========")
        print("1. Notatnik")
        print("2. Kalkulator")
        print("3. Visual Studio Code")
        print("4. Chrome")
        print("5. Eksplorator plików")
        print("6. Wpisz pełną ścieżkę do programu")
        print("7. Wyjście")
        print("================================")
        
        wybor = input("Wybierz opcję (1-7): ")
        
        if wybor == "1":
            open_program("C:\\Windows\\System32\\notepad.exe")
        elif wybor == "2":
            open_program("C:\\Windows\\System32\\calc.exe")
        elif wybor == "3":
            open_program("D:\\Microsoft VS Code\\Code.exe")
        elif wybor == "4":
            open_program("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif wybor == "5":
            open_program("C:\\Windows\\explorer.exe")
        elif wybor == "6":
            program = input("Podaj pełną ścieżkę do programu: ")
            open_program(program)
        elif wybor == "7":
            print("Do widzenia!")
            break
        else:
            print("✗ Niepoprawna opcja!")

menu()