import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import dblite

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


def main():
    url = "https://www.kvartirant.by/ads/rooms/type/rent/?tx_uedbadsboard_pi1%5Bsearch%5D%5Bq%5D=&tx_uedbadsboard_pi1%5Bsearch%5D%5Bdistrict%5D=80&tx_uedbadsboard_pi1%5Bsearch%5D%5Bprice%5D%5Bfrom%5D=80&tx_uedbadsboard_pi1%5Bsearch%5D%5Bprice%5D%5Bto%5D=130&tx_uedbadsboard_pi1%5Bsearch%5D%5Bcurrency%5D=840&tx_uedbadsboard_pi1%5Bsearch%5D%5Bdate%5D=2592000&tx_uedbadsboard_pi1%5Bsearch%5D%5Bowner%5D=on&tx_uedbadsboard_pi1%5Bsearch%5D%5Bremember%5D=1"
    data = requests.get(url)
    assert data.status_code == 200
    soup = BeautifulSoup(data.text, 'html.parser')
    apartments = soup.find("table", class_="ads_list_table").findAll("tr")

    path = os.getcwd()
    log = open(path + "/parser_log.txt", "w")
    log.write("TRY " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "\n\n\n")
    bad_apartment = None

    db = dblite.ApartmentsDb()

    try:
        i = 1
        for apartment in apartments:
            if "https://a.realt.by/www/delivery/ajs.php" not in str(apartment):
                bad_apartment = apartment
                title = apartment.find("p", class_="title")
                ap_url = title.find("a")['href']
                ap_id = ap_url.split("id")[1].replace("/", "", 2)
                log.write(str(i) + ") " + str(ap_url) + "\n")
                log.write("apartment id: " + ap_id + "\n")
                price = title.find("span").contents[0]
                log.write("price: " + str(price) + "\n")
                phone = apartment.find("span", class_="phones").find("img")['src']
                log.write("tel: " + str(phone) + "\n")
                ap_name = title.find("a").contents[0]
                log.write("name: " + str(ap_name) + "\n")
                owner = apartment.find("span", class_="phones").parent.contents[1]
                log.write("owner: " + str(owner) + "\n")
                log.write("about: ")
                about = ''.join(str(p.contents[0]).replace('<span class="rooms">', '')
                                  .replace('</span>', '').strip() for p in apartment.findAll("p", class_=None)[:-1])
                log.write(about)
                log.write("\n------------------------------\n")
                i += 1

                db.add_apartment(ap_id=ap_id, url=ap_url, price=price, phone=phone,
                                 ap_name=ap_name, owner=owner, about=about)

        log.write(db.get_apartments())

    except AttributeError:
        log.write("\n\n")
        log.write("!!!!!!!!!!!!!!!!!!!!!!!!! SOMETHING WENT WRONG WITH APARTMENT:\n")
        log.write(str(bad_apartment))
        log.write("!!!!!!!!!!!!!!!!!!!!!!!!!  \n\n")
    finally:
        log.close()


if __name__ == '__main__':
    main()
