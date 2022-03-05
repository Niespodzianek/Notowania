import requests

def connecting(page_www):
    try:
        odpowiedz = requests.get(page_www)
        print(odpowiedz.ok)
        print(odpowiedz.status_code)
    except requests.RequestException as error:
        print(f"Błąd przy połączeniu ze stroną {page_www}: {error}")
        return

    try:
        print(odpowiedz.raise_for_status())
    except requests.HTTPError as error:
        print(f"Żądanie zakończone niepowodzeniem: {error}")
        return
    zawartosc_strony = odpowiedz.text
    return zawartosc_strony

if __name__ == '__main__':
    page_html = input("Podaj adres strony www: ")
    page_html_text = connecting(page_www=page_html)
    print(page_html_text)
