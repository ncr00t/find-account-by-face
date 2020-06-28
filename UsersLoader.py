import vk_api
import codecs

if __name__ == '__main__':

    login = input('Enter login from VK:\n')
    password = input('Enter password from VK:\n')
    print('Enter params for search filter:\n\n')
    min_age = int((input('Enter min age:\n')))
    max_age = int((input('Enter max age:\n')))
    city_number = int((input('Enter city number:\n')))
    country_number = int((input('Enter country number:\n')))
    gender_number = int((input('Enter gender number:(female - 1, male - 2, any - 0)\n')))
    users_count = int((input('Enter max users count:\n')))
    search_words = input('Enter search words(first_name or last_name):\n')

    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    vk = vk_session.get_api()
    file_with_ids = codecs.open('ids.txt', 'w', encoding='utf8')
    users = vk.users.search(count=users_count,
                        fields='id, photo_max_orig, has_photo, '
                                'first_name, last_name',
                        q=search_words,
                        country=country_number,
                        city=city_number,
                        age_from=min_age,
                        age_to=max_age,
                        sex=gender_number)
    print('Peoples count: ' + str(users['count']))
    for x in users['items']:
      if x['has_photo'] == 1:
          s = str(x['id']) + '|' + str(x['photo_max_orig']) + '|' + str(
                  x['first_name']) + ' ' + str(x['last_name']) + '\n'
          file_with_ids.write(s)
          print(s)
    file_with_ids.close()
    print('Done!')


