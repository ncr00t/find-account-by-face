import shutil
import os
import requests
import codecs
import vk_api
import UsersLoader


def load_file(name, url):
    if not os.path.exists('jpg/' + str(name) + '.jpg'):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open('jpg/' + str(name) + '.jpg', 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)


def get_photos_by_id(user_id_, amount_uploaded_photos):
    try:
        response = vk.photos.getAll(owner_id=user_id_,
                                          count=amount_uploaded_photos,
                                          no_service_albums=0)
        prev = ''
        flag = 0
        photos = []
        for item in response['items']:
            for size in item['sizes']:
                url_ = str(size['url'])
                mas_ = url_.split('/')
                ident = mas_[4]
                if prev != ident:
                    prev = ident
                    flag = 0
                else:
                    flag += 1
                    if flag == 3:
                        photos.append(url_)
        max_flag = 0
        for photo in photos:
            max_flag += 1
            if max_flag < 10:
                load_file(str(user_id_) + '_' + str(max_flag), photo)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    login = UsersLoader.login
    password = UsersLoader.password

    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    vk = vk_session.get_api()
    user_info_file = codecs.open(u'ids.txt', 'r', encoding='utf8')

    amount_uploaded_photos = int((input('Enter amount uploaded for each user:\n')))

    amount_photos = 0
    for user_info in user_info_file:
        amount_photos += 1
        user_info_array = user_info.split('|')
        user_id = int(user_info_array[0])
        print('Amount photos: ' + str(amount_photos))
        get_photos_by_id(user_id, amount_uploaded_photos)
    user_info_file.close()
