import random
import os
import time

def symulacja_sesji_gieldowej(notowania):
    if notowania:
        zmiana_kursu = random.randrange(-10, 10)
        print(f"Kurs zmienił się o: {zmiana_kursu}%")
        aktualny_kurs = notowania[-1] + (zmiana_kursu / 100 * notowania[-1])
    else:
        aktualny_kurs = random.randrange(100, 200)
    print(f"Aktualny kurs: {aktualny_kurs:.2f}")
    return aktualny_kurs

def logika(notowania, notowanie):
    if len(notowania) == 0:
        print("Pierwsze notowanie. Otwarcie sesji giełdowej !!!")
    else:
        if notowanie > notowania[-1]:
            print("Kurs rośnie")
            if notowanie > max(notowania):
                print("Kurs poprawia maksymalny szczyt")
        elif notowanie < notowania[-1]:
            print("Kurs spada")
            if notowanie < min(notowania):
                print("Kurs osiągnął nowe minimum")
        else:
            print("Kurs pozostaje bez zmian")
    notowania.append(notowanie)
    return notowania

def srednia(srednie, notowania, dlugosc=3):
    if len(notowania) >= dlugosc:
        srednia_sma = sum(notowania[-dlugosc:]) / dlugosc
        srednie.append(srednia_sma)
        if len(srednie) >= 2:
            if notowania[-1] > srednie[-1] and notowania[-2] > srednie[-2]:
                print(f"Kurs kontynuuje średnioterminowy trend rosnący, kurs jest nad średnią z {dlugosc} sesji")
            elif notowania[-1] < srednie[-1] and notowania[-2] < srednie[-2]:
                print(f"Kurs kontynuuje średnioterminowy trend spadkowy, kurs jest pod średnią z {dlugosc} sesji")
            elif notowania[-1] > srednie[-1] and notowania[-2] < srednie[-2]:
                print(f"Kurs przebił od dołu średnią z {dlugosc} sesji - SYGNAŁ KUPNA")
            elif notowania[-1] < srednie[-1] and notowania[-2] > srednie[-2]:
                print(f"Kurs spadł poniżej średniej z {dlugosc} sesji - SYGNAŁ SPRZEDAŻY")
    return srednie

def logika_srednich(dluzsze_srednie, dluzsza, krotsze_srednie, krotsza):
    if len(dluzsze_srednie) > 2 and len(krotsze_srednie) > 2:
        if dluzsze_srednie[-1] < krotsze_srednie [-1] and dluzsze_srednie[-2] < krotsze_srednie[-2]:
            print(f"Średnie - kontynuacja trendu rosnącego. Średnia {krotsza} jest nad {dluzsza}. DŁUGOTERMINOWY WZROST")
        elif dluzsze_srednie[-1] > krotsze_srednie[-1] and dluzsze_srednie[-2] > krotsze_srednie[-2]:
            print(f"Średnie - kontynuacja trendu spadkowego. Średnia {dluzsza} jest nad {krotsza}. DŁUGOTERMINOWY SPADEK")
        elif dluzsze_srednie[-1] > krotsze_srednie[-1] and dluzsze_srednie[-2] < krotsze_srednie[-2]:
            print(f"Krótsza średnia {krotsza} przebiła od góry średnią {dluzsza}. SYGNAŁ ZMIANY DŁUGOTERMINOWEGO TRENDU NA SPADKOWY")
        elif dluzsze_srednie[-1] < krotsze_srednie[-1] and dluzsze_srednie[-2] > krotsze_srednie[-2]:
            print(f"Krótsza średnia {krotsza} przebiła od dołu średnią {dluzsza}. SYGNAŁ ZMIANY DŁUGOTERMINOWEGO TRENDU NA ROSNĄCY")
        elif dluzsze_srednie[-1] < krotsze_srednie[-1] and dluzsze_srednie[-2] == krotsze_srednie[-2]:
            print(f"Średnie - trend rosnący. Średnia {krotsza} jest nad {dluzsza}. DŁUGOTERMINOWY WZROST")
        elif dluzsze_srednie[-1] > krotsze_srednie[-1] and dluzsze_srednie[-2] == krotsze_srednie[-2]:
            print(f"Średnie - trend spadkowy. Średnia {krotsza} jest pod {dluzsza}. DŁUGOTERMINOWY SPADEK")
        elif dluzsze_srednie[-1] == krotsze_srednie[-1]:
            print(f"Średnia {krotsza} i średnia {dluzsza} zetknęły się.")
    return 0

def program():
    licznik = 0
    notowania = []
    srednie_sma_8 = []
    srednie_sma_21 = []
    while True:
        os.system("clear")
        print(f"Sesja nr: {licznik + 1}")
        licznik += 1
        notowanie = symulacja_sesji_gieldowej(notowania)
        notowania = logika(notowania, notowanie)
        srednie_sma_8 = srednia(srednie_sma_8, notowania, dlugosc=8)
        srednie_sma_21 = srednia(srednie_sma_21, notowania, dlugosc=21)
        logika_srednich(dluzsze_srednie=srednie_sma_21,dluzsza=21, krotsze_srednie=srednie_sma_8, krotsza=8)
        if srednie_sma_8 and srednie_sma_21:
            print(f"Kurs - otwarcie: {notowania[0]:.2f}, maks: {max(notowania):.2f}, min: {min(notowania):.2f}, ostatni:"
                  f" {notowania[-1]:.2f}, średnia SMA z 8 sesji: {srednie_sma_8[-1]:.2f} a z 21 sesji: {srednie_sma_21[-1]:.2f}")
        elif srednie_sma_8:
            print(f"Kurs - otwarcie: {notowania[0]:.2f}, maks: {max(notowania):.2f}, min: {min(notowania):.2f}, ostatni:"
                  f" {notowania[-1]:.2f}, średnia SMA z 8 sesji: {srednie_sma_8[-1]:.2f} a z 21 sesji: ---")
        else:
            print(f"Kurs - otwarcie: {notowania[0]:.2f}, maks: {max(notowania):.2f}, min: {min(notowania):.2f},"
                  f" ostatni: {notowania[-1]:.2f}, średnia SMA z 8 sesji: --- a z 21 sesji: ---")
        time.sleep(5)

if __name__ == "__main__":
    program()

#  TODO logika zależności pomiędzy aktualnym kursem a wskaźnikami takimi jak np.:
#  TODO 1. średnie, EMA
#  TODO 2. linie Boolingera
#  TODO 3. wykresy matplotlib
