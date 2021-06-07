import requests
from bs4 import BeautifulSoup

class Hisse():
    def __init__(self):
        url = "http://bigpara.hurriyet.com.tr/borsa/canli-borsa/en-cok-artanlar/"
        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi, "html.parser")

        veriler = soup.find_all("li", {"class": "cell064 tal arrow"})
        veriler2 = soup.find_all("li", {"class": "cell048 node-f"})
        veriler3 = soup.find_all("li", {"class": "cell048 node-g"})
        veriler4 = soup.find_all("li", {"class": "cell064 node-l"})

        liste = list()
        liste2 = list()
        liste3 = list()
        liste4 = list()
        for veri in veriler:
            veri = veri.text
            veri = veri.strip()
            liste.append(veri)
        for veri in veriler2:
            veri = veri.text
            veri = veri.strip()
            liste2.append(veri)
        for veri in veriler3:
            veri = veri.text
            veri = veri.strip()
            liste3.append(veri)
        for veri in veriler4:
            veri = veri.text
            veri = veri.strip()
            liste4.append(veri)

        self.hisse_Veriler = [liste[:10], liste2[:10], liste3[:10], liste4[:10]]

    def verileri_Getir(self):
        return self.hisse_Veriler

