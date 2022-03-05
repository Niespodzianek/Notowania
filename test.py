import statistics
odchylenie = 0
srednia = 0
lista = []

if len(lista) >= 2:
    odchylenie = statistics.stdev(lista[-10:])
elif len(lista) == 1:
    srednia = statistics.mean(lista[-10:])
print(f"średnia {srednia:.2f}, odchylenie: {odchylenie:.2f}, wstęga Bollingera Górna {(srednia + odchylenie):.2f}, Dolna {(srednia - odchylenie):.2f}")
