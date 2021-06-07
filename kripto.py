import requests
from bs4 import BeautifulSoup

class Kripto():
    def __init__(self):
        url = "https://tr.tradingview.com/markets/cryptocurrencies/prices-all/"
        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi, "html.parser")

        veriler = soup.find_all("a", {"class": "tv-screener__symbol"})
        veriler2 = soup.find_all("td", {"class": "tv-data-table__cell tv-screener-table__cell tv-screener-table__cell--big"})

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

        k_isimler = liste[:10]
        k_piyasa_degeri = liste2[0:50:6]
        k_k_k_s = liste2[3:53:6]
        k_islem_hacmi = liste2[5:55:6]

        self.kripto_Veriler = [k_isimler,k_piyasa_degeri,k_k_k_s,k_islem_hacmi]

    def verileri_Getir(self):
        return self.kripto_Veriler
