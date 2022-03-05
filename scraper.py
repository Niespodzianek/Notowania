from connector import connecting
import datetime
import time

def scraper(page_www):
    moment = datetime.datetime.now()
    # if moment.hour < 9:
    #     print("Jest jeszcze przed sesją giełdową")
    # elif moment.hour > 17:
    #     print("Jest już po sesji giełdowej")
    # else:
    #      = connecting(page_www)

    print(moment)
    input("Naciśnij ENTER")
    page_text = connecting(page_www)
    print(page_text)
    input("Naciśnij ENTER")

    start_index = page_text.index('<span id="aq_cri_c2"', 0)
    stop_index = page_text.index('>', start_index) + len('>')
    end_index = page_text.index('</span>', stop_index)
    price = page_text[stop_index:end_index]
    print(f"Kurs akcji: {price}")

if __name__ == '__main__':
    page_html = input("Podaj adres strony www:")
    licznik = 1
    while True:
        scraper(page_www=page_html)
        print(f"Krok {licznik}")
        time.sleep(10)
        licznik += 1
