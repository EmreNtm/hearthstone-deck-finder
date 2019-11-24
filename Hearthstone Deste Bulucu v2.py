import webbrowser
import requests
from bs4 import BeautifulSoup

print("***Class Seciniz!***\n")
print("1.Druid\n2.Hunter\n3.Mage\n4.Paladin\n5.Priest\n6.Rogue\n7.Shaman\n8.Warlock\n9.Warrior\n0.Hepsi")
a = int(input())
print("Lutfen bekleyin...")
if a == 1:
    url = "http://www.hearthpwn.com/decks?filter-deck-tag=4&filter-class=4&sort=-rating"
elif a == 2:
    url = "http://www.hearthpwn.com/decks?filter-deck-tag=4&filter-class=8&sort=-rating"
elif a == 3:
    url = "http://www.hearthpwn.com/decks?filter-deck-tag=4&filter-class=16&sort=-rating"
elif a == 4:
    url = "http://www.hearthpwn.com/decks?filter-deck-tag=4&filter-class=32&sort=-rating"
elif a == 5:
    url = "http://www.hearthpwn.com/decks?filter-deck-tag=4&filter-class=64&sort=-rating"
elif a == 6:
    url = "http://www.hearthpwn.com/decks?filter-deck-tag=4&filter-class=128&sort=-rating"
elif a == 7:
    url = "http://www.hearthpwn.com/decks?filter-deck-tag=4&filter-class=256&sort=-rating"
elif a == 8:
    url = "http://www.hearthpwn.com/decks?filter-deck-tag=4&filter-class=512&sort=-rating"
elif a == 9:
    url = "http://www.hearthpwn.com/decks?filter-deck-tag=4&filter-class=1024&sort=-rating"
else:
    url = "http://www.hearthpwn.com/decks?filter-deck-tag=4"

r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")

tablo = soup.find_all("table",{"class":"listing listing-decks b-table b-table-a"})

tablo1 = tablo[0].contents[3]

tablo1 = tablo1.find_all("tr")

x = int(input("Minimum puani girin: "))
print("\n******************************************************************************\n")
sira = 1
linkler = []
for deste in tablo1:
    deste_oyu = deste.find_all("td", {"class": "col-ratings"})
    deste_oyu = deste_oyu[0].find_all("div", {"class": "rating-sum rating-average rating-average-ratingPositive tip"})
    deste_oyu = deste_oyu[0].text
    if int(deste_oyu) >= x:
        deste_ismi = deste.find_all("td")
        deste_ismi = deste_ismi[0].find_all("div")
        deste_ismi = deste_ismi[0].find_all("span",{"class":"tip"})
        deste_linki = deste_ismi[0].find_all("a")
        deste_linki = deste_linki[0].get("href")
        deste_linki = "www.hearthpwn.com"+deste_linki
        linkler.append(deste_linki)
        deste_ismi = deste_ismi[0].text
        try:
            deste_tipi = deste.find_all("td",{"class":"col-deck-type"})
            deste_tipi = deste_tipi[0].find_all("span",{"class":"is-std"})
            deste_tipi = deste_tipi[0].text
        except(IndexError):
            deste_tipi = "Wild"
        print(sira,". ",deste_ismi," --> ",deste_tipi," --> ",deste_oyu,"\n")
        sira+=1
        print("******************************************************************************")
    else:
        p = tablo1[0].find_all("td", {"class": "col-ratings"})
        p = p[0].find_all("div", {"class": "rating-sum rating-average rating-average-ratingPositive tip"})
        p = p[0].text
        if int(p) < x:
            print("Bu kadar yüksek oylu deste bulunamadi!\n")
            break
        else:
            pass

while True:
    z = int(input("Deste seçmek için 1'i girin.\nÇıkmak için enter'a basın.\n"))
    if z == 1:
        try:
            print("Gitmek istediğiniz desteyi seçin.")
            sec = int(input())
            webbrowser.open(linkler[sec-1])
            break
        except(IndexError):
            print("Deste bulunamadı!")
            input("Programi kapatmak icin enter'a basin.")
            break
    else:
        break