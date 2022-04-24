import statistics
import random
import time
from matplotlib import pyplot as wykres

odchylenie = 0
srednia = 0
kolejnosc = []
lista = []
srednie = []
bbd = []
bd = []
bbg = []
bg = []
licznik = 0
dlugosc_sredniej = 2
while licznik < 50:
    licznik += 1
    kolejnosc.append(licznik)
    liczba = random.randrange(40, 60)
    lista.append(liczba)
    if len(lista) >= 2:
        odchylenie = statistics.stdev(lista[-dlugosc_sredniej:])
        srednia = statistics.mean(lista[-dlugosc_sredniej:])
        bbd.append(srednia - (2 * odchylenie))
        bd.append(srednia - odchylenie)
        bg.append(srednia + odchylenie)
        bbg.append(srednia + (2 * odchylenie))
    elif len(lista) == 1:
        srednia = statistics.mean(lista[-dlugosc_sredniej:])
        bbd.append(srednia)
        bd.append(srednia)
        bg.append(srednia)
        bbg.append(srednia)
    srednie.append(srednia)
    print(f"Notowanie {licznik}, BBD: {srednia - 2 * odchylenie:.2f}, BD: {srednia - odchylenie:.2f}, średnia: {srednia:.2f}, notowanie: {liczba}, BG: {srednia + odchylenie:.2f}, BBG: {srednia + 2 * odchylenie:.2f}")
    wykres.plot(kolejnosc, lista, color="blue")
    wykres.plot(kolejnosc, bbd)
    wykres.plot(kolejnosc, bd)
    wykres.plot(kolejnosc, srednie)
    wykres.plot(kolejnosc, bg)
    wykres.plot(kolejnosc, bbg)
    wykres.xlabel("Kolejne notowania")
    wykres.ylabel("Wartości")
    wykres.legend()
    wykres.show()
    time.sleep(10)
