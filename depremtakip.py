import requests
from bs4 import BeautifulSoup
import time

lastid = 0

kutuphane = []

rank = 0

while True:

    url = "https://deprem.afad.gov.tr/last-earthquakes.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table")
    rows = table.find_all("tr")

    degree = 0

    for i, row in enumerate(rows[:10]):
        cells = row.find_all("td")
        # Extract data from the cells
        if cells:
            date = cells[0].text.strip()
            longitude = cells[3].text.strip()
            magnitude = cells[5].text.strip()
            location = cells[6].text.strip()
            id = cells[7].text.strip()

            

            if id in kutuphane:
                continue
            else:
                magnitudecontrol = float(magnitude)
                if rank == 0 :
                    if degree == 0 :
                        if magnitudecontrol > 4 :
                            depremmessage = "🚨 Yeni Deprem !"
                            yermessage = "🗺️ Yer: " + location
                            magnitudemessage ="🔴 Büyüklük: " + magnitude
                            depthmessage = "⬇ Derinlik: " + longitude + " km"
                            tarihmessage = "📅 Tarih: " + date
                            kaynakmessage = "🟡Kaynak: AFAD"
                            degree = degree + 1
                            #"ID" ifadesi silinip Botfatherdaki Botun ID  ifadesi eklenecek. Örnek : bot6254350045:TAFllCCGZi-AtoP_Ooo5XFbGUgdTEt1NCbY
                            ap = "https://api.telegram.org/bot-BurayaIDGiriniz-/SendMessage"
                            #Chat id alanına ilgili chatin ID değeri girilecek örn: "-1108313129541"
                            requests.post(url=ap,data={"chat_id":"Burası Değişecek","text":depremmessage +  "\n\n" + yermessage + "\n\n" + magnitudemessage +
                            "\n\n" + depthmessage +
                            "\n\n" + tarihmessage +  "\n\n" + kaynakmessage}).json()
                    
                else:
                    if magnitudecontrol > 4 :
                        depremmessage = "🚨 Yeni Deprem !"
                        yermessage = "🗺️ Yer: " + location
                        magnitudemessage ="🔴 Büyüklük: " + magnitude
                        depthmessage = "⬇ Derinlik: " + longitude + " km"
                        tarihmessage = "📅 Tarih: " + date
                        kaynakmessage = "🟡Kaynak: AFAD"
                         #"ID" ifadesi silinip Botfatherdaki Botun ID  ifadesi eklenecek. Örnek : bot6254350045:TAFllCCGZi-AtoP_Ooo5XFbGUgdTEt1NCbY
                        ap = "https://api.telegram.org/bot-BurayaIDGiriniz-/SendMessage"
                        #Chat id alanına ilgili chatin ID değeri girilecek örn: "-1108313129541"
                        requests.post(url=ap,data={"chat_id":"Burası Değişecek","text":depremmessage +  "\n\n" + yermessage + "\n\n" + magnitudemessage +
                        "\n\n" + depthmessage +
                        "\n\n" + tarihmessage +  "\n\n" + kaynakmessage}).json()
                kutuphane.append(id)
                
    rank = rank + 1
    time.sleep(120)

