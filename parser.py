# -*- coding: utf-8 -*-"

import time
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from constants.constants import KVARTIRANT_URLS_TO_PARSE, KVARTIRANT_URL, IMAGES_COMMON_PATH
from domainObjects import flat
import mssqlProvider.mssqlProvider as database
from domainObjects.unparsedFlat import UnparsedFlat
from utils.requester import get
from utils.utils import write_file

from utils.utils import get_random_pause, create_directory_if_not_exist


def parse_kvartirant_apartments():
    for url in KVARTIRANT_URLS_TO_PARSE:
        request_data = get(url)
        soup = BeautifulSoup(request_data.text, 'html.parser')
        i = 0
        while True:
            next_page = soup.find("a", string="Следующая")
            parse_kvartirant_page(soup)
            if not next_page:
                break
            i += 1
            if i >= 30:
                break
            request_data2 = get(next_page["href"])
            soup = BeautifulSoup(request_data2.text, 'html.parser')
            time.sleep(get_random_pause())


def parse_exact_room_async(url, short_id):
    apartment = None

    request_data = get(url)
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
        create_directory_if_not_exist(IMAGES_COMMON_PATH + current_flat_temp.shortId)

        for image in soup.findAll("a", rel="pics"):
            write_file(IMAGES_COMMON_PATH + current_flat_temp.shortId + "\\" + image["href"].split("/")[-1],
                       get(KVARTIRANT_URL + image["href"]).content)
            __photosListUrls = __photosListUrls + image["href"].split("/")[-1] + ";"

        current_flat_temp.photosListUrls = __photosListUrls

        if current_flat_temp.phoneImgURL:
            write_file(IMAGES_COMMON_PATH + current_flat_temp.shortId + "\\" + current_flat_temp.phoneImgURL.split("/")[-1],
                       get(KVARTIRANT_URL + "/" + current_flat_temp.phoneImgURL).content)

        new_db = database.ApartmentsDb()
        new_db.add_apartment(current_flat_temp)
        new_db.con.close()

    except Exception as ex:
        broken_flat = UnparsedFlat()
        broken_flat.URL = str(url)
        broken_flat.HTML = str(apartment).replace("'", '"')
        broken_flat.Exception = str(ex).replace("'", '"')
        broken_flat.ErrorDate = datetime.now()
        new_db = database.ApartmentsDb()
        new_db.add_unpased_apartment(broken_flat)
        new_db.con.close()


def parse_kvartirant_page(soup):
    ap_url = None

    try:
        new_db = database.ApartmentsDb()
        existing_apartments_ids = new_db.get_exist_apartments_short_ids()
        new_db.con.close()

        apartments = soup.find("table", class_="ads_list_table").findAll("tr")

        for apartment in apartments:
            if "https://a.realt.by/www/delivery/ajs.php" not in str(apartment):
                try:
                    ap_url = apartment.find("p", class_="title").find("a")['href']
                    short_id = "kv" + ap_url.split("id")[1].replace("/", "", 2) \
                        .replace('"', '').replace("'", "")

                    if short_id not in existing_apartments_ids:
                        parse_exact_room_async(ap_url, short_id)

                except Exception as ex:
                    broken_flat = UnparsedFlat()
                    broken_flat.URL = str(ap_url)
                    broken_flat.HTML = str(apartment).replace("'", '"')
                    broken_flat.Exception = str(ex).replace("'", '"')
                    broken_flat.ErrorDate = datetime.now()
                    new_db = database.ApartmentsDb()
                    new_db.add_unpased_apartment(broken_flat)
                    new_db.con.close()

    except AttributeError as x:
        print("\n\n!!! error:\n" + str(x) + "!!!\n\n")


if __name__ == '__main__':
    parse_kvartirant_apartments()
