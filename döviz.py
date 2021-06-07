import requests
from bs4 import BeautifulSoup

class Doviz():
    def __init__(self):
        
        url = "https://www.bloomberght.com/doviz"
        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi, "html.parser")

        veriler = soup.find_all("td", {"style": "vertical-align:middle;"})

        liste = list()
        for veri in veriler:
            veri = veri.text
            veri = veri.strip()

            liste.append(veri)

        d_isimler = liste[1:-7:6]
        d_alis = liste[2:-6:6]
        d_satis = liste[3:-5:6]
        d_degisim = liste[4:-4:6]
        d_saat = liste[5:-3:6]

        self.doviz_Veriler = [d_isimler,d_alis,d_satis,d_degisim,d_saat]


    def verileri_Getir(self):
            return self.doviz_Veriler



