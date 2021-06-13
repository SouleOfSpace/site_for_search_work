from bs4 import BeautifulSoup
import requests, os
from fake_useragent import UserAgent

class ParserDevBy():
    def __init__(self):
        '''инициализация класса'''
        self.__url = 'https://jobs.dev.by/'
        self.__ua = UserAgent().firefox
        self.__headers = {
        'accept': 'text / html, application / xhtml + xml, application / xml; q = 0.9, image / avif, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange; v = b3; q = 0.9',
        'cookie': '_ym_uid = 1605730770132920541;_ym_d = 1605730770;_io_ht_r = 1;__io_first_source = google.com;__io_lv = 1611248622416; __io = 9a9debfa8.0eb2d3684_1611248622416; __io_pr_utm_campaign = % 7B % 22referrerHostname % 22 % 3A % 22www.google.com % 22 % 7D; __io_session_id = 1cf87711a.dabc6591e_1611248622419; __io_unique_12149 = 21; tariff_info_popup_skipped = false; _gid = GA1.2.399043432.1611248623; tmr_lvid = 02912bd54bd0c3651ee6a5ce2190655d; tmr_lvidTS = 1611248623183; _ym_visorc = w; _ym_isad = 2; _fbp = fb.1.1611248623517.351782499; wish_popup_skipped = true; _dev.by_session = BAh7CUkiD3Nlc3Npb25faWQGOgZFVEkiJTM0NDg5NzA0NTU5ZGRmZmI4MDQ4N2M3NjdjYWNjZDM2BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVpYdWNlTGt1cXdwRWNxZXdXbEt5TENBVGRVOGNUQTk5cmhldE8rRStqQVk9BjsARkkiEHJlZmVyZXJfdXJsBjsARiIZaHR0cHM6Ly9qb2JzLmRldi5ieS9JIgpmbGFzaAY7AFR7B0kiDGRpc2NhcmQGOwBUWwBJIgxmbGFzaGVzBjsAVHsGSSIZd2lzaF9zdWNjZXNzX21lc3NhZ2UGOwBURg % 3D % 3D - -01cada3873da996ac05e7590978160dde88adab7; __io_r = google.com; _ga_PBVMJ1K9WY = GS1.1.1611248622.1.1.1611250285.0; _ga = GA1.2.1870576182.1611248623; tmr_detect = 0 % 7C1611250288407; __io_d = 1_705468254; tmr_reqNum = 26',
        'user-agent': self.__ua
        }

    def get_links(self, class_for_links='vacancies-list-item__position'):
        '''Скрапер ссылок работ'''
        if (not isinstance(class_for_links, str)):
            raise TypeError

        if not self.check_connect():
            return 'Отсутствует интернет подключение'

        page = requests.get(url=self.__url, headers=self.__headers)
        # if page.status_code == 500:
        #     return 'Смените Id либо ожидайте пару минут для деблокировки'

        soup = BeautifulSoup(page.text, 'html.parser')
        links_on_work = []

        for i in soup.find_all('div', class_=class_for_links):
            full_link = self.create_link(i.a.get('href'))
            links_on_work.append(full_link)

        return links_on_work

    def create_link(self, half_link):
        '''Создание полной ссылки, с помощь которой, будет вытаскиваться информация о работе'''
        full_link = 'https://jobs.dev.by'+half_link
        return full_link

    def check_connect(self):
        '''Проверка на наличие интернет соеденения'''
        try:
            requests.get("http://google.com")
            return True
        except requests.exceptions.ConnectionError:
            return False

    def get_info_work(self, url='https://jobs.dev.by/vacancies/21509'):
        '''возвращает информацию о вакансии по переданной ссылке'''
        vacancy_info = {'link': '',
                         'Название': '',
                         'Специализация': '',
                         'Уровень': '',
                         'Опыт': '',
                         'Уровень английского': '',
                         'Зарплата': '',
                         'Город': '',
                         'Режим работы': '',
                         'Размер команды': '',
                         'Размер компании': '',
                         'Возможна удалённая работа': '',
                         'Агент': '',
                         'Тэги': '',
                         'Описание': ''
                         }   #словарь с полной информацией о вакансии

        vacancy_tags = []  # массив тэгов привязанных к данной вакансии
        description = ''    #строка, содержащая описание о вакансии
        page = requests.get(url=url, headers=self.__headers)    #страница html
        soup = BeautifulSoup(page.text, 'html.parser')          #soup страницы

        html_content = soup.find_all(class_='vacancy__info-block__item') #html с основной информацией
        html_tags = soup.find_all(class_='vacancy__tags__item')          #html с тегами вакансии
        html_description = soup.find_all(class_='vacancy__text')         #html с описанием вакансии

        # перебор и добавление в словарь основной информации
        for item in html_content:
            item_info = item.text.split(':')
            vacancy_info[item_info[0]] = item_info[1]

        # перебор и добавление в массив тегов о вакансии
        # for tag in html_tags:
        #     vacancy_tags.append(tag.text)
        vacancy_tags = self.get_vacancy_tags(url)

        # перебор и создание строки описания о вакансии
        # for item in html_description:
        #     description += description + item.text
        description = self.get_description(url)

        # if vacancy_info['Возможна удалённая работа'] == '': vacancy_info['Возможна удалённая работа'] = False
        # else: vacancy_info['Возможна удалённая работа'] = True
        vacancy_info['Возможна удалённая работа'] = self.get_talework(vacancy_info)

        vacancy_info['Название'] = soup.find(class_='title').text   # добавление в словарь названия вакансии
        vacancy_info['Агент'] = self.get_info_user(url=soup.find(class_='vacancy__agent__name').a.get('href'))# добавление в словарь агента вакансии
        vacancy_info['Тэги'] = vacancy_tags[0:-1]     # добавление в словарь массива тегов вакансии
        vacancy_info['Описание'] = description  # добавление в словарь описания вакансии

        return vacancy_info

    # tests
    def get_info_user(self, url):
        user_info = {'first_name': '',
                     'last_name': '',
                     'username': '',
                     'email': '',
                     }

        page = requests.get(url=url, headers=self.__headers)  # страница html
        soup = BeautifulSoup(page.text, 'html.parser')  # soup страницы

        user_info['first_name'] = soup.find(class_='profile__name').text.split(' ')[0]
        user_info['last_name'] = soup.find(class_='profile__name').text.split(' ')[1]
        user_info['username'] = soup.find(class_='profile__username').text
        user_info['email'] = soup.find(class_='mb-3 d-block').text
        # user_info['phone'] = soup.find_all(class_='island__item px-lg-0')[1].div.text
        # user_info['network'] = soup.find(class_='profile__row tag-group').a.get('href')

        return user_info

    #----utils fuctions-------------------------------------------------------------------------------------------------
    def get_vacancy_tags(self, url):
        # перебор и добавление в массив тегов о вакансии
        page = requests.get(url=url, headers=self.__headers)  # страница html
        soup = BeautifulSoup(page.text, 'html.parser')  # soup страницы
        html_tags = soup.find_all(class_='vacancy__tags__item')  # html с тегами вакансии
        vacancy_tags = []

        for tag in html_tags:
            vacancy_tags.append(tag.text)
        return vacancy_tags

    def get_description(self, url):
        # перебор и создание строки описания о вакансии
        page = requests.get(url=url, headers=self.__headers)  # страница html
        soup = BeautifulSoup(page.text, 'html.parser')  # soup страницы
        html_description = soup.find_all(class_='vacancy__text')  # html с описанием вакансии
        description = ''

        for item in html_description:
            description += description + item.text
        return description

    def get_talework(self, vacancy_info):
        if vacancy_info['Возможна удалённая работа'] == '': return False
        else: return True

if __name__ == '__main__':
    parser= ParserDevBy()
    print(parser.get_info_work('https://jobs.dev.by/vacancies/22770'))
