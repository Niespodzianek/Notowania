import statistics

lista = [100, 112, 134, 117, 109, 129, 134, 122, 120, 112, 108, 111, 121, 113]
srednia = statistics.mean(lista[-10:])
odchylenie = statistics.stdev(lista[-10:])
print(f"średnia {srednia:.2f}, odchylenie: {odchylenie:.2f}, wstęga Bollingera Górna {(srednia + odchylenie):.2f}, Dolna {(srednia - odchylenie):.2f}")
