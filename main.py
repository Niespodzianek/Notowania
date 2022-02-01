import random
import os


def symulacja_sesji_gieldowej():
    aktualny_kurs = random.randrange(100, 200)
    print(f"Aktualny kurs: {aktualny_kurs}")
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
    srednia = sum(notowania) / len(notowania)
    if notowanie > srednia:
        print("Kurs jest powyżej średniej")
    elif notowanie < srednia:
        print("Kurs jest poniżej średniej")
    else:
        print("Kurs jest równy średniej")
    print(
        f"Kurs - otwarcie: {notowania[0]}, maks: {max(notowania)}, min: {min(notowania)}, ostatni: {notowania[-1]}, "
        f"średnia: {srednia}"
    )
    input("Naciśnij ENTER aby kontynuować")
    return notowania


def program():
    notowania = []
    while True:
        os.system("clear")
        notowanie = symulacja_sesji_gieldowej()
        notowania = logika(notowania, notowanie)
        print(notowania)


if __name__ == "__main__":
    program()

#  TODO logika zależności pomiędzy aktualnym kursem a wskaźnikami takimi jak np.:
#  TODO 1. średnie
#  TODO 2. linie Boolingera
#  TODO 3. wykresy matplotlib
