# -*- coding: utf-8 -*-"

from urllib.request import urlretrieve
import vk, os, time, math
import config
from dblite import ApartmentsDb
import requests


class VkWrapper:
    """Class-wrapper for vk package"""

    def __init__(self, vk_app_id=None, login=None, password=None):
        """Method-constructor for vk wrapper
        """
        if login and password and vk_app_id:
            self.session = vk.AuthSession(app_id=vk_app_id, access_token=config.acces_token)
        else:
            self.session = vk.Session()
        self.vk_api = vk.API(self.session)

    # https://vk.com/id103092544?z=album103092544_204454841
    def save_album_photo_by_album_url(self, url):
        album_id = url.split('/')[-1].split('_')[1]
        owner_id = url.split('album')[-1].split('_')[0].replace('album', '')
        print(album_id, owner_id)

        photos_count = self.vk_api.photos.getAlbums(owner_id=owner_id, album_ids=album_id)[0]['size']

        counter = 0  # текущий счетчик
        prog = 0  # процент загруженных
        breaked = 0  # не загружено из-за ошибки
        time_now = time.time()  # время старта
        error_urls = []


        # Создадим каталоги
        if not os.path.exists('saved'):
            os.mkdir('saved')
        photo_folder = 'saved/album{0}_{1}'.format(owner_id, album_id)
        if not os.path.exists(photo_folder):
            os.mkdir(photo_folder)

        for j in range(math.ceil(photos_count / 1000)):  # Подсчитаем сколько раз нужно получать список фото, так как число получится не целое - округляем в большую сторону
            print(str(j))
            photos = self.vk_api.photos.get(owner_id=owner_id, album_id=album_id, count=1000,
                                            offset=j * 1000)  # Получаем список фото
            print(str(photos))
            for photo in photos:
                counter += 1
                url = photo.get('src_xbig', 'src_big')  # Получаем адрес изображения
                print('Загружаю фото № {} из {}. Прогресс: {} %'.format(counter, photos_count, prog))
                prog = round(100 / photos_count * counter, 2)
                try:
                    urlretrieve(url, photo_folder + "/" + os.path.split(url)[1])  # Загружаем и сохраняем файл
                except Exception:
                    error_urls.append({'url': url, 'photo': photo})
                    print('Произошла ошибка, файл пропущен.')
                    breaked += 1
                    continue

        time_for_dw = time.time() - time_now
        print("\nВ очереди было {} файлов. Из них удачно загружено {} файлов, {} не удалось загрузить. "
              "Затрачено времени: {} сек.".format(photos_count, photos_count - breaked, breaked, round(time_for_dw, 1)))

    def add_post(self, message):
        post = self.vk_api.wall.post(owner_id=config.vk_group_id, message=message, version=config.vk_api_version)
        return post['post_id']

    def upload_photo_to_server_and_post_on_my_wall(self, img_name):
        upload_url = self.vk_api.photos.getWallUploadServer(owner_id=None)['upload_url']

        # Формируем данные параметров для сохранения картинки на сервере
        request = requests.post(upload_url, files={'photo': open(img_name, "rb")})
        print(request.json())
        params = {'server': request.json()['server'],
                  'photo': request.json()['photo'],
                  'hash': request.json()['hash'],
                  'owner_id': None}

        # Сохраняем картинку на сервере и получаем её идентификатор
        photo_id = self.vk_api.photos.saveWallPhoto(**params)[0]['id']

        # Формируем параметры для размещения картинки в группе и публикуем её
        params = {'attachments': photo_id,
                  'owner_id': None,
                  'from_group': '1'}
        self.vk_api.wall.post(**params)

    def upload_photo_to_server(self, photo_string):
        # data = self.vk_api.photos.getUploadServer(user_id="449873763",
        #                                           album_id=config.vk_group_photo_album_numbers,
        #                                           headers={'Content-Type': "multipart/form-data"},
        #                                           file=open('Penguins.jpg', 'rb'))
        # print(data)
        # data2 = self.vk_api.photos.save(album_id=data['aid'], server=data['upload_url'])
        # print(data2)
        upload_url = self.vk_api.photos.getWallUploadServer(owner_id=None)['upload_url']

        # Формируем данные параметров для сохранения картинки на сервере
        request = requests.post(upload_url, files={'photo': open("Penguins.jpg", "rb")})
        print(request.json())
        params = {'server': request.json()['server'],
                  'photo': request.json()['photo'],
                  'hash': request.json()['hash'],
                  'owner_id': None}

        # Сохраняем картинку на сервере и получаем её идентификатор
        photo_id = self.vk_api.photos.saveWallPhoto(**params)[0]['id']

        # Формируем параметры для размещения картинки в группе и публикуем её
        params = {'attachments': photo_id,
                  'owner_id': None,
                  'from_group': '1'}
        self.vk_api.wall.post(**params)


if __name__ == "__main__":
    ap = ApartmentsDb().get_apartments()
    q = requests.get("https://www.kvartirant.by/typo3temp/GB/21334a7bd7.gif")
    VkWrapper(vk_app_id=config.vk_app_id, login=config.login, password=config.password).upload_photo_to_server(photo_string=q.content)
    # post_message = """{ap_name}\n{about}\n{price}\n{owner}\n{phone}""".format(ap_name=ap[0]['ap_name'],
    #                                                                           about=ap[0]['about'],
    #                                                                           price=ap[0]['price'],
    #                                                                           owner=ap[0]['owner'],
    #                                                                           phone=q.content)
    # VkWrapper(vk_app_id=config.vk_app_id, login=config.login, password=config.password).add_post(message=post_message)
