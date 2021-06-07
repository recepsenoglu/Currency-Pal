import requests
from bs4 import BeautifulSoup

class Altin():
    def __init__(self):
        url = "http://bigpara.hurriyet.com.tr/altin/"
        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi, "html.parser")

        veriler = soup.find_all("li", {"class": "cell010 tal"})
        veriler2 = soup.find_all("li", {"class": "cell009"})

        liste = list()
        liste2 = list()
        for veri in veriler:
            veri = veri.text
            veri = veri.strip()
            liste.append(veri)

        for veri in veriler2:
            veri = veri.text
            veri = veri.strip()
            liste2.append(veri)

        a_isimler = liste[1:-4:]
        a_alis = liste2[4:-16:4]
        a_satis = liste2[5:-15:4]
        a_degisim = liste2[6:-14:4]
        a_saat = liste2[7:-13:4]

        self.altin_Veriler = [a_isimler,a_alis,a_satis,a_degisim,a_saat]

    def verileri_Getir(self):
        return self.altin_Veriler

