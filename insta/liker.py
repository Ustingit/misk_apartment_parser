# https://selenium-python.readthedocs.io/installation.html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from random import randrange
import os

insta_url = "https://www.instagram.com/"
insta_url2 = "https://www.instagram.com"

USED_LIST = []


def random_sleep():
    sleep(randrange(10))


def like_it(user):
    driver = webdriver.Chrome()
    driver.get(insta_url)
    driver.maximize_window()

    log_in_button = driver.find_element_by_xpath("//a[.='Вход']")  #("Log in")
    log_in_button.click()

    sleep(2)

    username_input = driver.find_element_by_xpath("//input[@name='username']")
    username_input.clear()
    username_input.send_keys("+375298386116")
    sleep(2)
    password__input = driver.find_element_by_xpath("//input[@name='password']")
    password__input.clear()
    password__input.send_keys("Guitarpro9Instagram")

    enter_button = driver.find_element_by_xpath("//button[@type='submit']")
    enter_button.click()
    sleep(2)

    driver.get(insta_url + user)
    sleep(2)
    assert user in driver.title

    followers_button = driver.find_element_by_xpath("//a[contains(@href,'/followers/')]")
    followers_button.click()

    sleep(2)

    for url in list(set([follower.get_attribute("href") for follower in driver.find_elements_by_xpath("//div/ul/div/li//a")])):
        #actions = ActionChains(driver)
        #actions.move_to_element(follower).perform()  # driver.execute_script("arguments[0].scrollIntoView();", element)
        if is_not_used_user(url, get_used_from_file()):
            print(url)
            driver.get(url)

            try:
                first_image = driver.find_element_by_xpath("(//article//img/../../../..)[1]")
                first_image.click()
                sleep(3)

                like_button = driver.find_element_by_xpath("//article//section//span[contains(@class, 'Heart') and contains(@class, 'outline')]/..")
                like_button.click()
                save_used_to_file(url.split('com')[1].replace('/', '', 10))
                random_sleep()
            except Exception as ex:
                print(ex)

    driver.close()


def is_not_used_user(url, list_users):
    result = True
    for user in list_users:
        if user in url and user != '':
            result = False
    return result


def get_used_from_file():
    return read_file().split(';')


def save_used_to_file(data=None):
    write_file(data)


def read_file(write_path='./usedUsers.txt'):
    with open(write_path, 'r') as f:
        return f.read()


def write_file(data, separator=';', write_path='./usedUsers.txt', mode='a'):
    if not os.path.exists(write_path):
        mode = 'w'
    with open(write_path, mode) as f:
        f.write(data + separator)


if __name__ == "__main__":
    like_it("evtushenko905")

"""
https://www.instagram.com/sourabh_daksh_/
https://www.instagram.com/ermashechka/
https://www.instagram.com/_wot_blitz_account_ru_eu/
https://www.instagram.com/kule_male/
https://www.instagram.com/shahad_.k/
https://www.instagram.com/amazing_toyss/
https://www.instagram.com/almuhari84/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/foootball__video/
https://www.instagram.com/bestdeck_054/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/alexsander_moiseev/
https://www.instagram.com/kaz_football_kaz/
https://www.instagram.com/briguithamoros/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/persik__slimes/
https://www.instagram.com/kolesniknikita04/
https://www.instagram.com/dimos_thrash_tattoo/
https://www.instagram.com/benonator06/
https://www.instagram.com/darya.traven/
https://www.instagram.com/gadanie33444/
https://www.instagram.com/aida_salon/
https://www.instagram.com/bohdan22853/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"//article//section//span[contains(@class, 'Heart') and contains(@class, 'outline')]/.."}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/iunkhen26/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/1043ka/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/slahaljmay65/
https://www.instagram.com/rheal_bullet/
https://www.instagram.com/asamoah.pamela/
https://www.instagram.com/keny_blaq/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/isaacdamba6/
https://www.instagram.com/ay3l63/
https://www.instagram.com/oxygraphics/
https://www.instagram.com/richkhalifa758gmail.com9/
https://www.instagram.com/nharnhar_ama_cutie/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/peprahderick/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/motibee/
https://www.instagram.com/currencyba/
https://www.instagram.com/asdh99510/
https://www.instagram.com/roselvert_blackson/
https://www.instagram.com/theophiluzscratch/
https://www.instagram.com/liksi533/
https://www.instagram.com/jonu2255/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/gonylom/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"//article//section//span[contains(@class, 'Heart') and contains(@class, 'outline')]/.."}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/sviatoslav5030/
https://www.instagram.com/holin2323/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"//article//section//span[contains(@class, 'Heart') and contains(@class, 'outline')]/.."}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/andriukhach/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/appcombin/
https://www.instagram.com/alijoni_7/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/goalkeepermka135208/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/sv1ntus/
https://www.instagram.com/simo_abb.08/
https://www.instagram.com/augusta_aleksandr_696/
https://www.instagram.com/kenmojeyk/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/xx_e_l_3_4_r_y/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/gfxgxfddsa/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"//article//section//span[contains(@class, 'Heart') and contains(@class, 'outline')]/.."}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/any7official/
https://www.instagram.com/_.mkot._fenya_/
https://www.instagram.com/holster.ua/
https://www.instagram.com/anna_riznyk1207/
https://www.instagram.com/sasha02950/

https://www.instagram.com/alisadulebo_/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"//article//section//span[contains(@class, 'Heart')]/.."}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/1.namozov.m/
https://www.instagram.com/okulik95/
https://www.instagram.com/matzip_storm_/
https://www.instagram.com/lomako_dashaa_05/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/grom.nikito/
https://www.instagram.com/pyrakondasha/
https://www.instagram.com/nasty_novik06/
https://www.instagram.com/artjoms2002/
https://www.instagram.com/b_boy_dranik/
https://www.instagram.com/alisadulebo_prvt/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/marinalotysh/
https://www.instagram.com/1617svetlana/
https://www.instagram.com/l9l94ka/
https://www.instagram.com/alisa_grin/
https://www.instagram.com/snezha_511/
https://www.instagram.com/nikita.grishchuk/
https://www.instagram.com/_princeeeess._/
https://www.instagram.com/max_yaskul/
https://www.instagram.com/33brut/
https://www.instagram.com/buryibear95/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/m_a_s_h_a_603/
https://www.instagram.com/maslovamashka/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/ksusha.kovalevskay/
https://www.instagram.com/victoria_kontrova/
https://www.instagram.com/lidiiaprokhorevich/
https://www.instagram.com/mironovadiana31/
https://www.instagram.com/tatiana_shid/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"//article//section//span[contains(@class, 'Heart')]/.."}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/daria_sarnatskaia/
https://www.instagram.com/vl_ad7285/
https://www.instagram.com/marusyazenko/
https://www.instagram.com/kovalevskaya.ksusha/
https://www.instagram.com/angelina_patalei/
https://www.instagram.com/viktoria_kontrova/
https://www.instagram.com/aliiinkaa_maliinkaa/
https://www.instagram.com/vladermolaev6845/
https://www.instagram.com/1166sasha/
https://www.instagram.com/apollinaria.an/
https://www.instagram.com/katty_mwk/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/kirill__bond/
https://www.instagram.com/sputnikanskie_elfy/
https://www.instagram.com/motsna.by/
https://www.instagram.com/oleja_kazeko/
https://www.instagram.com/pavel______kozel/
https://www.instagram.com/damskiy_ugodnik20017/
https://www.instagram.com/varia_52019/
https://www.instagram.com/staspikuza092019/
https://www.instagram.com/bushido_karate_club_riga/
https://www.instagram.com/katayra.san/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/melnik005/
https://www.instagram.com/el_prolet/
https://www.instagram.com/ivanshurvel99/
https://www.instagram.com/roman_gorbachev2006/
https://www.instagram.com/popoval_2005_k.mbappe/
https://www.instagram.com/chiara_massagrande/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/khomykhhomyh/
https://www.instagram.com/ekaterina.yatsura/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/elisaweta_lis/
https://www.instagram.com/khomich186/
https://www.instagram.com/valerir08/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/nastyaket284/
https://www.instagram.com/nikita_plesushkin/
https://www.instagram.com/nikita.grishchuk/
https://www.instagram.com/batvilovskaya_polina/
https://www.instagram.com/staspikuza09/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"//article//section//span[contains(@class, 'Heart')]/.."}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/iyaskul/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/ilia18936/
https://www.instagram.com/karate_gleb/
https://www.instagram.com/babyfoodkz/
https://www.instagram.com/abramovic_katya/
https://www.instagram.com/angelinafilippovich/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/angelina.4272/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/kudryashka_sofia/
https://www.instagram.com/anastasia_78964/
https://www.instagram.com/masha.4060/
https://www.instagram.com/mamsik.kz_/
https://www.instagram.com/arinych20/
https://www.instagram.com/kulieva3208/
https://www.instagram.com/mila_ice___cream/
https://www.instagram.com/mandarinka_2007_/
https://www.instagram.com/nikita_kents/
https://www.instagram.com/fominapolina15/
https://www.instagram.com/privat__milanaaa/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/kigurumi_detkam/
https://www.instagram.com/erjan228007/
https://www.instagram.com/__mc_enot__/
https://www.instagram.com/artom_fg/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/kostochka_barabanov/
https://www.instagram.com/_nacow/
https://www.instagram.com/fanatkkabts/
https://www.instagram.com/vadime_kent/
https://www.instagram.com/drawings_bangtana/
https://www.instagram.com/chunjingyi/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/dicarocarballude/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/danayapolkova/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/levan_sonia/
https://www.instagram.com/elizavetta_raluk/
https://www.instagram.com/juliya_top_master_shugaring/
https://www.instagram.com/elenpolkova/
https://www.instagram.com/nikolai1804206/
https://www.instagram.com/vika_li12/
https://www.instagram.com/bts_love_a.r.m.y_love_bts/

https://www.instagram.com/first_choice_tyres/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/leg_auto_body_repair/
https://www.instagram.com/volat_club_belarus/
https://www.instagram.com/school4cherven/
https://www.instagram.com/nastasiahappiness/
https://www.instagram.com/pikuzaalex81/
https://www.instagram.com/varia_52019/
https://www.instagram.com/leliashingirei/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/boosk_karate_minsk/
https://www.instagram.com/victoria_kontrova/
https://www.instagram.com/glebizminska/
https://www.instagram.com/katty_mwk/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/talyansyy/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/pavel______kozel/
https://www.instagram.com/ksusha.kovalevskay/
https://www.instagram.com/kostya_feofanov111/
https://www.instagram.com/pooolllllyyyyy/
https://www.instagram.com/m_a_s_h_a_603/
https://www.instagram.com/cherven__manicure/
https://www.instagram.com/_prodigal_daughter666/
https://www.instagram.com/viktoria_kontrova/
https://www.instagram.com/jollygrisha91/
https://www.instagram.com/itsksyusha_/
https://www.instagram.com/ksyushashevchuk/
https://www.instagram.com/angelina_patalei/
https://www.instagram.com/1166sasha/
https://www.instagram.com/swadba.by/
https://www.instagram.com/polinaioksha/
https://www.instagram.com/igo3099/
https://www.instagram.com/daria_sarnatskaia/
https://www.instagram.com/hot_red_girl99/
https://www.instagram.com/alexandrapolozkova8468/
https://www.instagram.com/prikaza.liene/
https://www.instagram.com/alya_freydlih4676/
https://www.instagram.com/ricardskrivins/
https://www.instagram.com/tutubook/
https://www.instagram.com/mazaa_ciepinja/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/bagdantnt/
https://www.instagram.com/fabio.bangrazi_fbcoach/
https://www.instagram.com/nellija_vorobjova/
https://www.instagram.com/fastemilio100/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/desford_2675/
https://www.instagram.com/fannybartoneduce/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/malyshechka_/
https://www.instagram.com/inkaviski/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.142)

https://www.instagram.com/victori_93/
https://www.instagram.com/debora_macaluso/
https://www.instagram.com/grom.nikito/
https://www.instagram.com/tvoyo.solnishko55/
https://www.instagram.com/alen4zv/
https://www.instagram.com/evelina_lasmane/
https://www.instagram.com/normenskrilkovs/
https://www.instagram.com/karinaagorbachova/
https://www.instagram.com/silvajaudzeme/
https://www.instagram.com/beate.augule/
https://www.instagram.com/andruha_shok/

https://www.instagram.com/sofiavoropay_3/
https://www.instagram.com/carbonatcalciya/
https://www.instagram.com/lora.satsukevich/
https://www.instagram.com/interfotoby/
https://www.instagram.com/karateeleanore/
https://www.instagram.com/dasha_ivarovskaya/
https://www.instagram.com/parikmakherskaiaul.ia.luchiny/
https://www.instagram.com/kataglobal/
https://www.instagram.com/tvoyo.solnishko55/
https://www.instagram.com/nikita.grishchuk/
https://www.instagram.com/arawazaby/
https://www.instagram.com/staspikuza092019/
https://www.instagram.com/aleksandrataradula/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"//article//section//span[contains(@class, 'Heart')]/.."}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/troyanovskaya.tatsiana/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/vladimirvladimirovichpoliakov/
https://www.instagram.com/moto_podbor.bel/

https://www.instagram.com/rebrova742/
https://www.instagram.com/aleksandrf144/
https://www.instagram.com/mageranastasya/
https://www.instagram.com/stinging_cherry/
https://www.instagram.com/fedo595/
https://www.instagram.com/kmo.2015.14/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"//article//section//span[contains(@class, 'Heart')]/.."}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/german4455066/
https://www.instagram.com/anna_sinyavskay10/
https://www.instagram.com/varia_52019/
https://www.instagram.com/milanadashchinskaya/
https://www.instagram.com/hot_red_girl99/
https://www.instagram.com/postcrossing_sanya10/
https://www.instagram.com/mariya_siadzko17_/
https://www.instagram.com/alism.a/
https://www.instagram.com/wokebombin/
https://www.instagram.com/kovalevskaya.ksusha/
https://www.instagram.com/sonya_06__/
https://www.instagram.com/footballclass_by/
https://www.instagram.com/de10rken/
https://www.instagram.com/ksusha.kovalevskay/
https://www.instagram.com/yana__22__/
https://www.instagram.com/dytyachi_tovary/
https://www.instagram.com/k_evgenii83/
https://www.instagram.com/ctrekoza.smy/
https://www.instagram.com/giliana_sugar/
https://www.instagram.com/irinasavsun/
https://www.instagram.com/dianamateush_14/
https://www.instagram.com/alibekxujamberdiyev/
https://www.instagram.com/englisharabic/
https://www.instagram.com/camgonespazz/
https://www.instagram.com/liutik.vania/
https://www.instagram.com/nazim_mohamed__/
https://www.instagram.com/mameri00/
https://www.instagram.com/lwise_salah/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/__.8viktoria8.__/
https://www.instagram.com/labfair/
https://www.instagram.com/_vikschiks_/
https://www.instagram.com/alina_olegovna44/
https://www.instagram.com/han_k_m_1845/
https://www.instagram.com/t_etyana8/
https://www.instagram.com/ghofran_aldroubi/
https://www.instagram.com/empregandodf/
https://www.instagram.com/niksebe/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/anna.olegovna852/
https://www.instagram.com/silvio_napolitano/

Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/malusheva_oksana/
https://www.instagram.com/kiga_boom/
https://www.instagram.com/pp.t.win.s/
https://www.instagram.com/kira_gan123/
https://www.instagram.com/angelinafilippovich/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/zinahoroha/
https://www.instagram.com/____privat_s____/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/airpods_shop.by/
https://www.instagram.com/levan_sonia/
https://www.instagram.com/patoloesa/
https://www.instagram.com/elena.baliabina/
https://www.instagram.com/delina665/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/katya2005.20/
https://www.instagram.com/gumanovasvetlana/
https://www.instagram.com/aldamsk/
https://www.instagram.com/aldamsk_2/
https://www.instagram.com/katty_mwk/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/mashs916/
https://www.instagram.com/christina__inst/
https://www.instagram.com/estelshopby/
https://www.instagram.com/andreevasvetlana45/
https://www.instagram.com/mitrakovao/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/natalinchik33/
https://www.instagram.com/tatiana.matiushonok/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/svetlana_avsiyevich/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/kameneva3458/
https://www.instagram.com/ve_ra/
https://www.instagram.com/kseniiakragelskaia/
https://www.instagram.com/mkazev.maksim1999/
https://www.instagram.com/veryaevanadezhda/
https://www.instagram.com/dmitrij_naklej_legostaev/
https://www.instagram.com/blizko_by/
https://www.instagram.com/marina_novik197/
https://www.instagram.com/melestovaelena/
https://www.instagram.com/natallia_kosach/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/ni4ka.ba4ishe/
https://www.instagram.com/m.zhadan/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/kozhokinruslan/
https://www.instagram.com/kotova.sanya/
https://www.instagram.com/mitr750/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/misspati_2/
https://www.instagram.com/kvestbel/
https://www.instagram.com/egorkorolev7/
https://www.instagram.com/alexandrapolozkova8468/
https://www.instagram.com/nikabobko/
https://www.instagram.com/nicatbaxsov113452019/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/akulicsofa/
https://www.instagram.com/hot_red_girl99/
https://www.instagram.com/nail_coke/
https://www.instagram.com/ianasemizhon/
https://www.instagram.com/viktoria_kontrova/
https://www.instagram.com/zohaib_pirada/
https://www.instagram.com/m_a_s_h_a_603/
https://www.instagram.com/eleevaaleksandra/
https://www.instagram.com/de10rken/
https://www.instagram.com/in_dreams_02/
https://www.instagram.com/nastuaana/
https://www.instagram.com/polina.13vitko/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/denisevichkate/
https://www.instagram.com/tat.zakurdaeva/
https://www.instagram.com/angelina_patalei/
https://www.instagram.com/ogopolina/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/shqwf6540/
https://www.instagram.com/slaim2428/
https://www.instagram.com/eva_zhuravleva909/
https://www.instagram.com/kovalevskaya.ksusha/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"//article//section//span[contains(@class, 'Heart')]/.."}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/dsarnackaa/
https://www.instagram.com/_viazka_/
https://www.instagram.com/abramovic_katya/
https://www.instagram.com/football__weekdays/
https://www.instagram.com/liza_slimes2019/
https://www.instagram.com/rostkay/
https://www.instagram.com/sergey_buts5/
https://www.instagram.com/pavelbionchik/
https://www.instagram.com/de10rken/
https://www.instagram.com/space_devil666/
https://www.instagram.com/____privat_s____/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/liotrender/
https://www.instagram.com/daria_sarnatskaia/
https://www.instagram.com/_kred0_/
https://www.instagram.com/ksu_privatiikkk/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/tereshkevichkseniia/
https://www.instagram.com/timolik/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/katty_mwk/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/olehka_solnce/
https://www.instagram.com/stinging_cherry/
https://www.instagram.com/mashs916/
https://www.instagram.com/_skalaba_/
https://www.instagram.com/benzzo_shooter/
https://www.instagram.com/nikabobko/
https://www.instagram.com/ksyushashevchuk/
https://www.instagram.com/val_born/
https://www.instagram.com/snus_lion.rb/
https://www.instagram.com/suren.privat/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/kovalevskaya.ksusha/
https://www.instagram.com/__1_asia_6__/
https://www.instagram.com/hot_red_girl99/
https://www.instagram.com/pavel______kozel/
https://www.instagram.com/m_a_s_h_a_603/
https://www.instagram.com/valeriakorz9/
https://www.instagram.com/_otritsaniye_/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/tenderlybae.cc/
https://www.instagram.com/fasolkon_4.0/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/vita_9086/
https://www.instagram.com/polinaioksha/
https://www.instagram.com/makeenkoantonina5/
https://www.instagram.com/__daiano4ka__/
https://www.instagram.com/locks.by/
https://www.instagram.com/dasha_shibalovich/

https://www.instagram.com/buryibear95/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/viktoria_kontrova/
https://www.instagram.com/1166sasha/
https://www.instagram.com/kirill__bond/
https://www.instagram.com/oleja_kazeko/
https://www.instagram.com/maslovamashka/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"//article//section//span[contains(@class, 'Heart')]/.."}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/katty_mwk/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/kovalevskaya.ksusha/
https://www.instagram.com/m_a_s_h_a_603/
https://www.instagram.com/_interstellllar_/
https://www.instagram.com/victoria_kontrova/
https://www.instagram.com/angelina_patalei/

https://www.instagram.com/glebizminska/
https://www.instagram.com/polinaioksha/
https://www.instagram.com/alexandrapolozkova8468/
https://www.instagram.com/igo3099/
https://www.instagram.com/_prodigal_daughter666/
https://www.instagram.com/viktoria_kontrova/
https://www.instagram.com/kostya_feofanov111/
https://www.instagram.com/vita_9086/
https://www.instagram.com/hot_red_girl99/
https://www.instagram.com/katty_mwk/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/talyansyy/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/victoria_kontrova/
https://www.instagram.com/cherven__manicure/
https://www.instagram.com/1166sasha/
https://www.instagram.com/ksyushashevchuk/
https://www.instagram.com/angelina_patalei/
https://www.instagram.com/itsksyusha_/
https://www.instagram.com/m_a_s_h_a_603/


https://www.instagram.com/silicone_case_minsk_belarus/
https://www.instagram.com/tallianaricardo/
https://www.instagram.com/kj8318kj/
https://www.instagram.com/marseli_salon/
https://www.instagram.com/irin_realty/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/aisul___hk/
https://www.instagram.com/anastasia_140798/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/mnogo_deneg_real/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"//article//section//span[contains(@class, 'Heart')]/.."}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/trinalavskaya/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/potolki_vgomele/
https://www.instagram.com/catalina_vogue/
https://www.instagram.com/dorriane_michelle/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/mariam_ahmed1660/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/askn_banu_can/
https://www.instagram.com/lerikayasya/
https://www.instagram.com/dariafedorako/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/sergeevich4175/
https://www.instagram.com/polinka_radkevich/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/klimovich9701/
https://www.instagram.com/helenamandrik/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/litvinenko_sviatoslav/
https://www.instagram.com/l.m.s.1086/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/_am_selly_/

https://www.instagram.com/anate311287/
https://www.instagram.com/karunnikovaanastasiia/
https://www.instagram.com/decor.vika/
https://www.instagram.com/instup.bel/
https://www.instagram.com/sannyant/
https://www.instagram.com/momdocha_shop_by/
https://www.instagram.com/toy_story_blrs/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/polirovka_volos_zodino_borisov/
https://www.instagram.com/ketimihailova60gmail.com_/
https://www.instagram.com/modeli.vminske/
https://www.instagram.com/lilianna_gryzunki/
https://www.instagram.com/kantsmarket.by/
https://www.instagram.com/zlata.zolotaya/
https://www.instagram.com/anfisport/
https://www.instagram.com/shargelminsk/
https://www.instagram.com/kovrochistka/
https://www.instagram.com/kritik4788/
https://www.instagram.com/classydressboutique/
https://www.instagram.com/svetloiarko1/
https://www.instagram.com/baraholka_pyatigorsk26/
https://www.instagram.com/sales4you_here/
https://www.instagram.com/anna_wedding.by/
https://www.instagram.com/fitness_marafon_minsk/

ustin\AppData\Local\Programs\Python\Python36-32\python.exe D:/parser/new_clone/misk_apartment_parser/insta/liker.py
https://www.instagram.com/moda_krasota1990/
https://www.instagram.com/natali_29d/
https://www.instagram.com/kachar_hamrawi/
https://www.instagram.com/faraj_khan_8708/
https://www.instagram.com/sveta.latset94/
https://www.instagram.com/natalinchik33/
https://www.instagram.com/janna_kravchenko_1/
https://www.instagram.com/vikuliasha2011/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/amirka_867/
https://www.instagram.com/prismascalamayor/
https://www.instagram.com/zeptervminske/
https://www.instagram.com/julie_m_95/
https://www.instagram.com/sheelasaab2255/
https://www.instagram.com/kukhniishkafy/
https://www.instagram.com/valentinazales/
https://www.instagram.com/lavana_studio/
https://www.instagram.com/sedykevich/
https://www.instagram.com/fort_soxf/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/rahimov186/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/vij2300/
https://www.instagram.com/mutekar_bhimashankar/
https://www.instagram.com/alt_stone/
https://www.instagram.com/maminkalapuzik/
https://www.instagram.com/greenway.eco.1/
https://www.instagram.com/andreimikhailouski/
https://www.instagram.com/bulavki.imennye.belarus/
https://www.instagram.com/bazapostavshshikov2019/
https://www.instagram.com/6malcll/
https://www.instagram.com/oktyabr_mocuzesi6/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"//article//section//span[contains(@class, 'Heart')]/.."}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/alexa_shop_by/
https://www.instagram.com/anyaklimova7/
https://www.instagram.com/ksuyasen1/
https://www.instagram.com/rymia_alimova/
https://www.instagram.com/bruta9704/
https://www.instagram.com/a.stories_modnaia.by/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/baza_leila/
https://www.instagram.com/look_shop_belarus/
https://www.instagram.com/motherbags.by/
https://www.instagram.com/bo_nata_/
https://www.instagram.com/viza_for_you/
https://www.instagram.com/girl_spark_/
https://www.instagram.com/fisherbeautyroom/
https://www.instagram.com/watchmaker.by/
https://www.instagram.com/shop_barportal/
https://www.instagram.com/sasha0287s/
https://www.instagram.com/_yulia_07_/
https://www.instagram.com/successuspeh1/
https://www.instagram.com/boevayaclassica_of/
https://www.instagram.com/nastya_key_11/
https://www.instagram.com/kati.kamliuk/
https://www.instagram.com/ve.ro1556/
https://www.instagram.com/zhukliudmila9/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"//article//section//span[contains(@class, 'Heart')]/.."}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/nastya_vasileva_2905/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/the.world.of.avatars/
https://www.instagram.com/pavel___kabanov/
https://www.instagram.com/labykoliudmila/
https://www.instagram.com/yanka_390/
https://www.instagram.com/andreizhmoidyak/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/artokynev/
https://www.instagram.com/alekseenko__tatiana/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/vania_rysev/
https://www.instagram.com/vivachel/
https://www.instagram.com/yulia_mak_20/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/viktoria_kontrova/
https://www.instagram.com/vitalik_suvorov3/
https://www.instagram.com/ig_or1489/
https://www.instagram.com/ioannaseverin/
https://www.instagram.com/eleevaaleksandra/
https://www.instagram.com/verytupaya__maybeangela/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/yanka_xlam/
https://www.instagram.com/trestian_/
https://www.instagram.com/_k_s_e_n_i_a_267/
https://www.instagram.com/p_i_e_s_h_o_p/
https://www.instagram.com/veronika.2803_/
https://www.instagram.com/dresscode_minsk/
https://www.instagram.com/bboy_enotik_krutoy/
https://www.instagram.com/__angel_privat.__/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/_tmaks_/
https://www.instagram.com/zero_znakomstv/
https://www.instagram.com/agromovaonelove/
https://www.instagram.com/paulina_agromova/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/____.d.o.r.o.h.o.v.i.c.h.____/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/iilomilllo/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/vikaokyneva/
https://www.instagram.com/_makryxa_ga_/
https://www.instagram.com/sasha_zzz__erc/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/best_nails_minsk77/
https://www.instagram.com/sidorenko.lena.00/
https://www.instagram.com/kamenigor37/
https://www.instagram.com/_taduruk_/
https://www.instagram.com/vovakurlovich_/
https://www.instagram.com/minsk_for_you/
https://www.instagram.com/_littele_angel_/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/sa_sha4918/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/baranovanastia4412/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/discone.in.ua/
https://www.instagram.com/_kirasor_privat_/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/best_of_korea.as/
https://www.instagram.com/tema.zet/
https://www.instagram.com/snaiper.olga01986/
Message: no such element: Unable to locate element: {"method":"xpath","selector":"(//article//img/../../../..)[1]"}
  (Session info: chrome=75.0.3770.100)

https://www.instagram.com/hot_red_girl99/
https://www.instagram.com/workshop_marina/
https://www.instagram.com/_interstellllar_/
https://www.instagram.com/kovalevskaya.ksusha/

//used:

"""