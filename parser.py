# -*- coding: utf-8 -*-"

import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os
import random
# import unixNotifier
from domainObjects import flat
import mssqlProvider.mssqlProvider as database
from domainObjects.unparsedFlat import UnparsedFlat
import os


def get_random_pause():
    return random.randint(1, 3)


def parse_kvartirant_apartments():
    log = open(os.getcwd() + "/parser_log.txt", "w")
    log.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "\n\n\n")

    urls = ['https://www.kvartirant.by/ads/flats/type/rent/', 'https://www.kvartirant.by/ads/rooms/type/rent/?tx_uedbadsboard_pi1%5Bsearch%5D%5Bq%5D=&tx_uedbadsboard_pi1%5Bsearch%5D%5Bdistrict%5D=0&tx_uedbadsboard_pi1%5Bsearch%5D%5Bprice%5D%5Bfrom%5D=80&tx_uedbadsboard_pi1%5Bsearch%5D%5Bprice%5D%5Bto%5D=130&tx_uedbadsboard_pi1%5Bsearch%5D%5Bcurrency%5D=840&tx_uedbadsboard_pi1%5Bsearch%5D%5Bdate%5D=2592000&tx_uedbadsboard_pi1%5Bsearch%5D%5Bowner%5D=on']
    try:
        for url in urls:
            request_data = requests.get(url)
            if request_data.status_code == 200:
                soup = BeautifulSoup(request_data.text, 'html.parser')
                i =0
                while True:
                    next_page = soup.find("a", string="Следующая")
                    parse_kvartirant_page(log, soup)
                    if not next_page:
                        break
                    i += 1
                    if i >= 30:
                        break
                    request_data2 = requests.get(next_page["href"])
                    if request_data2.status_code == 200:
                        soup = BeautifulSoup(request_data2.text, 'html.parser')
                    time.sleep(get_random_pause())
    finally:
        log.close()


def parse_exact_room_async(url, logger, short_id):
    request_data = requests.get(url)
    apartment = None
    if request_data.status_code == 200:
        try:
            soup = BeautifulSoup(request_data.text, 'html.parser')
            apartment = soup.find("div", class_="adtxt_box")

            current_flat_temp = flat.Flat()
            title = apartment.find("p", class_="title")
            current_flat_temp.sourceURL = url
            current_flat_temp.shortId = short_id
            current_flat_temp.price = title.find("span").contents[0]
            current_flat_temp.name = title.find("span").parent.contents[-1]
            current_flat_temp.author = apartment.find("span", class_="phones").parent.contents[1]
            current_flat_temp.description = (''.join(str(p.contents[0]).replace('<span class="rooms">', '').replace('</span>', '').strip() for p in apartment.findAll("p", class_=None)[:-1])).replace('"', '', 100).replace("'", "", 100)
            current_flat_temp.phoneImgURL = apartment.find("span", class_="phones").find("img")['src']
            current_flat_temp.creationDate = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")
            current_flat_temp.actualToDate = (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d %H:%M:%S.%f")
            current_flat_temp.parsingSource = 1
            current_flat_temp.isActive = 1
            current_flat_temp.clientId = 1
            __photosListUrls = ""

            path = "D:\\parser\\new_clone\\misk_apartment_parser\\images\\kvartirant\\" + current_flat_temp.shortId
            if not os.path.exists(path):
                os.makedirs(path)

            for image in soup.findAll("a", rel="pics"):
                response = requests.get("https://www.kvartirant.by" + image["href"])
                if response.status_code == 200:
                    with open("D:\\parser\\new_clone\\misk_apartment_parser\\images\\kvartirant\\"
                              + current_flat_temp.shortId + "\\" + image["href"].split("/")[-1], 'wb') as f:
                        __photosListUrls = __photosListUrls + image["href"].split("/")[-1] + ";"
                        f.write(response.content)

            current_flat_temp.photosListUrls = __photosListUrls

            if current_flat_temp.phoneImgURL:
                response2 = requests.get("https://www.kvartirant.by/" + current_flat_temp.phoneImgURL)
                if response2.status_code == 200:
                    with open("D:\\parser\\new_clone\\misk_apartment_parser\\images\\kvartirant\\"
                              + current_flat_temp.shortId + "\\" + current_flat_temp.phoneImgURL.split("/")[-1], 'wb') as f:
                        f.write(response2.content)

            newDB = database.ApartmentsDb()
            newDB.add_apartment(current_flat_temp)
            newDB.con.close()

        except Exception as ex:
            logger.write(str(ex))

            broken_flat = UnparsedFlat()
            broken_flat.URL = str(url)
            broken_flat.HTML = str(apartment).replace("'", '"')
            broken_flat.Exception = str(ex).replace("'", '"')
            broken_flat.ErrorDate = datetime.now()
            newDB = database.ApartmentsDb()
            newDB.add_unpased_apartment(broken_flat)
            newDB.con.close()


def parse_kvartirant_page(logger, soup):
    ap_url = None

    try:
        newDB = database.ApartmentsDb()
        existingApartmentsIds = newDB.get_exist_apartments_short_ids()
        newDB.con.close()

        apartments = soup.find("table", class_="ads_list_table").findAll("tr")

        for apartment in apartments:
            if "https://a.realt.by/www/delivery/ajs.php" not in str(apartment):
                try:
                    ap_url = apartment.find("p", class_="title").find("a")['href']
                    short_id = "kv" + ap_url.split("id")[1].replace("/", "", 2) \
                        .replace('"', '').replace("'", "")

                    if short_id not in existingApartmentsIds:
                        parse_exact_room_async(ap_url, logger, short_id)

                except Exception as ex:
                    logger.write(str(ex))

                    broken_flat = UnparsedFlat()
                    broken_flat.URL = str(ap_url)
                    broken_flat.HTML = str(apartment).replace("'", '"')
                    broken_flat.Exception = str(ex).replace("'", '"')
                    broken_flat.ErrorDate = datetime.now()
                    newDB = database.ApartmentsDb()
                    newDB.add_unpased_apartment(broken_flat)
                    newDB.con.close()

    except AttributeError as x:
        logger.write("\n\n!!! error:\n" + str(x) + "!!!\n\n")


if __name__ == '__main__':
    parse_kvartirant_apartments()
