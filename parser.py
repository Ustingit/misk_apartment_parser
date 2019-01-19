# -*- coding: utf-8 -*-"

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import dblite
#import unixNotifier
import flat
import mssqlProvider.mssqlProvider as database


def parse_kvartirant_apartments():
    #notif = unixNotifier.UnixNotifier("There is new apartment in Minsk (from kvartirant):")
    url = "https://www.kvartirant.by/ads/rooms/type/rent/?tx_uedbadsboard_pi1%5Bsearch%5D%5Bq%5D=&tx_uedbadsboard_pi1%5Bsearch%5D%5Bdistrict%5D=80&tx_uedbadsboard_pi1%5Bsearch%5D%5Bprice%5D%5Bfrom%5D=80&tx_uedbadsboard_pi1%5Bsearch%5D%5Bprice%5D%5Bto%5D=130&tx_uedbadsboard_pi1%5Bsearch%5D%5Bcurrency%5D=840&tx_uedbadsboard_pi1%5Bsearch%5D%5Bdate%5D=2592000&tx_uedbadsboard_pi1%5Bsearch%5D%5Bowner%5D=on&tx_uedbadsboard_pi1%5Bsearch%5D%5Bremember%5D=1"
    data = requests.get(url)
    assert data.status_code == 200
    soup = BeautifulSoup(data.text, 'html.parser')
    apartments = soup.find("table", class_="ads_list_table").findAll("tr")

    log = open(os.getcwd() + "/parser_log.txt", "w")
    log.write("TRY " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "\n\n\n")
    bad_apartment = None

    db = dblite.ApartmentsDb()
    exist_aps = db.get_exist_apartments_ids()

    newDB = database.ApartmentsDb()
    existingApartmentsIds = newDB.get_exist_apartments_ids()

    try:
        i = 1
        for apartment in apartments:
            if "https://a.realt.by/www/delivery/ajs.php" not in str(apartment):
                try:
                    current_flat = flat.Flat()
                    bad_apartment = apartment
                    title = apartment.find("p", class_="title")
                    ap_url = title.find("a")['href']
                    current_flat.ap_url = ap_url
                    current_flat.ap_id = int(ap_url.split("id")[1].replace("/", "", 2).replace('"', '').replace("'", ""))
                    current_flat.price = title.find("span").contents[0]
                    current_flat.ap_name = title.find("a").contents[0].replace('"', '').replace("'", "")
                    current_flat.owner = apartment.find("span", class_="phones").parent.contents[1]
                    current_flat.about = (''.join(str(p.contents[0]).replace('<span class="rooms">', '')
                                .replace('</span>', '').strip() for p in apartment.findAll("p", class_=None)[:-1]))\
                                .replace('"', '', 100).replace("'", "", 100)
                    current_flat.phone = apartment.find("span", class_="phones").find("img")['src']
                    i += 1
                    if current_flat.ap_id not in exist_aps:
                        db.add_apartment(current_flat)


                except Exception as ex:
                    log.write(str(ex))

    except AttributeError:
        log.write("\n\n!!!!!!!!!!!!!!!!!!!!!!!!! SOMETHING WENT WRONG WITH APARTMENT:\n")
        log.write(str(bad_apartment) + "!!!!!!!!!!!!!!!!!!!!!!!!!  \n\n")
    finally:
        log.close()
        db.con.close()


def qwe(): pass


if __name__ == '__main__':
    parse_kvartirant_apartments()








# Print out the results to screen
    # for t in findPatTitle:
    #     pic_name = os.path.basename(t)
    #     with contextlib.closing(urlopen(t, 'rb')) as pic:
    #         p = pic.read()
    #         if len(p) > 1000:
    #             print
    #             t  # The title
    #             with open(pic_name, 'wb') as of:
    #                 of.write(p)
    #             webbrowser.open(pic_name)


# url = 'https://r.onliner.by/ak/?price[min]=50&price[max]=120&currency=usd#bounds[lb][lat]=53.767789993998804&bounds[lb][long]=27.36625671386719&bounds[rt][lat]=54.02794011027586&bounds[rt][long]=27.757644653320316'
# def main():
#     headers = {"Content-Type": "Application/json", "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}
#     data = requests.get(url)
#     print(data.text)
#     assert data.status_code == 200
#     soup = BeautifulSoup(data.text, 'html.parser')
#     apartments = soup.find_all("a", href=lambda href: href and "https://r.onliner.by/ak/apartments/" in href)
#     for i in apartments:
#         print("A: " + str(i))
#         print("-----------------")
#     # apartments = div.select("a[href*=https://r.onliner.by/ak/apartments/]")
