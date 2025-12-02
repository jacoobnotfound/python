#program do obliczania rzeczywistego rozmiaru obiektu na podstawie skali mapy

skala = input("podaj skale (bez 1:): ")
na_mapie = input("podaj rozmiar na mapie: ")

# Konwersja na liczby
skala = int(skala)
na_mapie = float(na_mapie)

# Obliczanie rzeczywistego rozmiaru
rzeczywisty_rozmiar = na_mapie * skala

print(f"\nSkala: 1:{skala}")
print(f"Rozmiar na mapie: {na_mapie}")
print(f"Rzeczywisty rozmiar: {rzeczywisty_rozmiar}")

# Dodatkowe informacje
if rzeczywisty_rozmiar >= 1000:
    rozmiar_km = rzeczywisty_rozmiar / 1000
    print(f"Rzeczywisty rozmiar: {rozmiar_km} km")
else:
    print(f"Rzeczywisty rozmiar: {rzeczywisty_rozmiar} m")