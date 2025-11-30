import json

with open("todo.json", "r") as f:
    todo = json.load(f)


wybor = ""

def menu():
    while True:
        print("=========== TODO LIST ===========")
        print("1. Dodaj do listy")
        print("2. Usuń z listy")
        print("3. Oznacz jako zrobione")
        print("4. Wypisz Listę")
        print("5. Wyjdź")
        wybor = int(input("co chcesz zrobić: "))
        if wybor == 1:
            add_to_todo()
        if wybor == 2:
            reamove_from_list()
        if wybor == 3:
            mark_as_done()
        if wybor == 4:
            print(todo)
        if wybor == 5:
            break


def add_to_todo():
    ToAdd = input("co chcesz dodać do listy TODO: ")
    todo.append(ToAdd)
    print(todo)
    with open("todo.json", "w") as f:
        json.dump(todo, f)
def reamove_from_list():
    try:
        ToRem = int(input("które pole chcesz usunąć?(0-{}): ".format(len(todo) - 1)))
        if 0 <= ToRem < len(todo):
            removed_item = todo.pop(ToRem)
            print(f"Usunięto: {removed_item}")
            with open("todo.json", "w") as f:
                json.dump(todo, f)
        else:
            print("Nieprawidłowy indeks.")
    except ValueError:
        print("Proszę podać liczbę całkowitą.")

def mark_as_done():
    try:
        ToDone = int(input("które pole chcesz oznączyć jako zrobione?(0-{}): ".format(len(todo) - 1)))
        if 0 <= ToDone < len(todo):
            todo[ToDone] = todo[ToDone] + " ✓"
            print(f"Oznaczono jako zrobione: {todo[ToDone]}")
            with open("todo.json", "w") as f:
                json.dump(todo, f)
        else:
            print("Nieprawidłowy indeks.")
    except ValueError:
        print("Proszę podać liczbę całkowitą.")

menu()