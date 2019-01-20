# -*- coding: utf-8 -*-"

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os
# import unixNotifier
import flat
import mssqlProvider.mssqlProvider as database
from domainObjects.unparsedFlat import UnparsedFlat


def parse_kvartirant_apartments():
    # notif = unixNotifier.UnixNotifier("There is new apartment in Minsk (from kvartirant):")
    url = "https://www.kvartirant.by/ads/rooms/type/rent/?tx_uedbadsboard_pi1%5Bsearch%5D%5Bq%5D=&tx_uedbadsboard_pi1%5Bsearch%5D%5Bdistrict%5D=80&tx_uedbadsboard_pi1%5Bsearch%5D%5Bprice%5D%5Bfrom%5D=80&tx_uedbadsboard_pi1%5Bsearch%5D%5Bprice%5D%5Bto%5D=130&tx_uedbadsboard_pi1%5Bsearch%5D%5Bcurrency%5D=840&tx_uedbadsboard_pi1%5Bsearch%5D%5Bdate%5D=2592000&tx_uedbadsboard_pi1%5Bsearch%5D%5Bowner%5D=on&tx_uedbadsboard_pi1%5Bsearch%5D%5Bremember%5D=1"
    data = requests.get(url)
    assert data.status_code == 200
    soup = BeautifulSoup(data.text, 'html.parser')
    apartments = soup.find("table", class_="ads_list_table").findAll("tr")

    log = open(os.getcwd() + "/parser_log.txt", "w")
    log.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "\n\n\n")
    bad_apartment = None
    global_ap_url = None

    newDB = database.ApartmentsDb()
    existingApartmentsIds = newDB.get_exist_apartments_short_ids()

    try:
        for apartment in apartments:
            if "https://a.realt.by/www/delivery/ajs.php" not in str(apartment):
                try:
                    current_flat = flat.Flat()
                    bad_apartment = apartment
                    title = apartment.find("p", class_="title")
                    ap_url = title.find("a")['href']
                    global_ap_url = ap_url
                    current_flat.sourceURL = ap_url
                    current_flat.shortId = "kv" + ap_url.split("id")[1].replace("/", "", 2) \
                        .replace('"', '').replace("'", "")
                    current_flat.price = title.find("span").contents[0]
                    current_flat.name = title.find("a").contents[0].replace('"', '').replace("'", "")
                    current_flat.author = apartment.find("span", class_="phones").parent.contents[1]
                    current_flat.description = (''.join(str(p.contents[0]).replace('<span class="rooms">', '')
                                                        .replace('</span>', '').strip() for p in
                                                        apartment.findAll("p", class_=None)[:-1])) \
                        .replace('"', '', 100).replace("'", "", 100)
                    current_flat.phoneImgURL = apartment.find("span", class_="phones").find("img")['src']
                    current_flat.creationDate = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")
                    current_flat.actualToDate = (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d %H:%M:%S.%f")
                    current_flat.parsingSource = 1
                    current_flat.isActive = 1
                    current_flat.clientId = 1
                    newDB.add_apartment(current_flat)

                except Exception as ex:
                    log.write(str(ex))

                    broken_flat = UnparsedFlat()
                    broken_flat.URL = str(global_ap_url)
                    broken_flat.HTML = str(bad_apartment).replace("'", '"')
                    broken_flat.Exception = str(ex).replace("'", '"')
                    broken_flat.ErrorDate = datetime.now()
                    newDB.add_unpased_apartment(broken_flat)

    except AttributeError:

        log.write("\n\n!!! SOMETHING WENT WRONG WITH APARTMENT:\n" + str(bad_apartment) + "!!!\n\n")
    finally:
        log.close()
        newDB.con.close()


if __name__ == '__main__':
    parse_kvartirant_apartments()
