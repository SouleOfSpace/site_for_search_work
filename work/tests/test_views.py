from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.models import Tag
from django.core.exceptions import AppRegistryNotReady

from work.models import Post, Newswork, Resume
from work import views
from utils import parser_dev_by

from unittest.mock import patch, Mock

class TestViews(TestCase):
    '''pass'''

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='name', password='admin', email='a@mail.ru', first_name='sasha',
                                        last_name='volosevich')
        self.user_admin = User.objects.create_user(username='admin', password='admin', email='ad@mail.ru', first_name='sasha',
                                 last_name='volosevich')

        self.post = Post.objects.create(
                            link='https://test.ru',
                            title='title',
                            talework=True,
                            agent=self.user,
                            size_company=20,
                            # slug='test_slug'
                            )
        Post.objects.create(
            link='https://test2.ru',
            title='title2',
            talework=True,
            agent=self.user,
            size_company=20,
            # slug='test_slug'
        )
        self.tag = Tag.objects.create(name='tag')

        self.news = Newswork.objects.create(agent = self.user,
                                            title='title',
                                            body='body',
                                            ).save()

        self.post_list_url = reverse('work:post_list')
        self.post_list_by_tags = reverse('work:post_list_by_tags', args=['tag'])
        self.post_detail = reverse('work:post_detail', args=['2021', '6', '13', 'title', '1'])
        self.post_create = reverse('work:post_create')
        self.post_list_by_search = reverse('work:search')

        self.newswork_detail = reverse('work:news_detail', args=['title', '1'])
        self.resume_create = reverse('work:resume_create', args=[1,])

        self.url_create_auto_post = reverse('work:post_create_auto')

#----test_post_list-----------------------------------------------------------------
    def test_post_list_GET(self):
        '''post_list с отправленной не валидной формой GET - должны получить HTML'''
        response = self.client.get(self.post_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/post/list.html')

    def test_post_list_POST(self):
        '''post_list с отправленной формой POST - должны получить HTML'''
        response = self.client.post(self.post_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/post/list.html')

    def test_post_list_whithData_1(self):
        '''Вызов страницы со списком вакансий по поисковому слову, з двух вакансий найдет только одну'''
        response = self.client.get(self.post_list_url, {'query': ['title2']})

        received_obj = len(response.context['page_obj'])
        expected_obj = 1

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/post/list.html')
        self.assertEqual(received_obj, expected_obj)

    def test_post_list_by_tags_GET(self):
        '''Вызов страницы со списком вакансий отсортированных по тегу'''
        response = self.client.get(self.post_list_by_tags)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/post/list.html')
#-----------------------------------------------------------------------------------

#----test_post_detail---------------------------------------------------------------
    def test_post_detail_GET(self):
        '''Вызов страницы с детольным описанием вакансии'''
        response = self.client.get(self.post_detail)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/post/detail.html')

# ----test_create_post--------------------------------------------------------------
    def test_create_post_validWithTags_ready(self):
        '''Создание вакансии с добавлением тегов'''
        Post.objects.all().delete()
        self.client.login(username='admin', password='admin')

        response = self.client.post(self.post_create, {
                            'link': 'https://www.sadasd.ru',
                            'title': 'test',
                            'specialization': 'Не важно',
                            'level': 'Не важно',
                            'experience': 'Не важно',
                            'level_english': 'Любой',
                            'salary': 'Не важно',
                            'city': 'Не важно',
                            'mode_work': 'Не важно',
                            'size_team': '',
                            'size_company': 30,
                            'talework': True,
                            'description': 'asd',
                            'status': 'active',
                            'tags': 'tag, tag2'
        })

        received = response.context['status']
        expected = 'ready'

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/post/create.html')
        self.assertEqual(received, expected)

    def test_create_post_POSTwithoutTags_creating(self):
        '''Создание вакансии без добавления тегов вызовет ошибку, т.к. поле с тегами обязательно к заполнению'''
        Post.objects.all().delete()

        self.client.login(username='admin', password='admin')
        response = self.client.post(self.post_create, {
            'link': 'https://www.sadasd.ru',
            'title': 'test',
            'specialization': 'Не важно',
            'level': 'Не важно',
            'experience': 'Не важно',
            'level_english': 'Любой',
            'salary': 'Не важно',
            'city': 'Не важно',
            'mode_work': 'Не важно',
            'size_team': '',
            'size_company': 20,
            'talework': True,
            'description': 'asd',
            'status': 'active',
            'Тэги': ''
        })

        received = response.context['status']
        expected = 'creating'

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/post/create.html')
        self.assertEqual(received, expected)

    def test_create_post_notValid_creating(self):
        '''Создание вакансии не прошедшее валидацию'''
        Post.objects.all().delete()

        self.client.login(username='admin', password='admin')
        response = self.client.post(self.post_create, {})

        received = response.context['status']
        expected = 'creating'

        self.assertEqual(response.status_code, 200)
        self.assertEqual(received, expected)

    def test_create_post_GET(self):
        '''Создание вакасии методом гет'''
        Post.objects.all().delete()
        self.client.login(username='admin', password='admin')

        response = self.client.get(self.post_create, {
            'link': 'https://www.sadasd.ru',
            'title': 'test',
            'specialization': 'Не важно',
            'level': 'Не важно',
            'experience': 'Не важно',
            'level_english': 'Любой',
            'salary': 'Не важно',
            'city': 'Не важно',
            'mode_work': 'Не важно',
            'size_team': '',
            'size_company': 20,
            'talework': True,
            'description': 'asd',
            'status': 'active',
        })

        received = response.request['REQUEST_METHOD']
        expected = 'GET'

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/post/create.html')
        self.assertEqual(received, expected)
#-----------------------------------------------------------------------------------

#----post_list_by_search------------------------------------------------------------
    def test_post_list_by_search_GET(self):
        '''Расширенный пооиск вакансии вызванный методом ГЕТ'''
        response = self.client.get(self.post_list_by_search)

        received = response.request['REQUEST_METHOD']
        expected = 'GET'

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/post/search.html')
        self.assertEqual(received, expected)

    def test_post_list_by_search_notValid_NotValid(self):
        '''Расширенный поиск вакансии с невалидной формой'''
        response = self.client.post(self.post_list_by_search, {"title": '1234jknkjn5678901234567890'})
        received = response.context['status']
        expected = 'Not valid'

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/post/search.html')
        self.assertEqual(received, expected)

    def test_post_list_by_search_ValidWithoutSizeCompany_1(self):
        '''Расширенный поиск вакансии без указания размера компании'''
        response = self.client.post(self.post_list_by_search, {
                                        'title': 'title2',
                                        'specialization': '',
                                        'level': '',
                                        'experience': '',
                                        'level_english': '',
                                        'salary': '',
                                        'city': '',
                                        'mode_work': '',
                                        'size_company': 'None',
                                        'talework': True,})

        received = len(response.context['posts'])
        expected = 1

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/post/search.html')
        self.assertEqual(received, expected)

    def test_post_list_by_search_ValidWithSizeCompany_1(self):
        '''Расширенный поиск вакансии с указание размера компании'''
        response = self.client.post(self.post_list_by_search, {
            'title': 'title2',
            'specialization': '',
            'level': '',
            'experience': '',
            'level_english': '',
            'salary': '',
            'city': '',
            'mode_work': '',
            'size_company': '0,40',
            'talework': True, })

        received = len(response.context['posts'])
        expected = 1

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/post/search.html')
        self.assertEqual(received, expected)

#----newswork_detail-------------------------------------------------------------------------
    def test_newswork_detail_GET(self):
        '''Вызов страницы с детольным описанием новости'''
        response = self.client.get(self.newswork_detail)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/newswork/detail.html')
#---------------------------------------------------------------------------------------------

#----create_resume----------------------------------------------------------------------------
    def test_create_resume_GET(self):
        '''Вызов функции методом ГЕТ'''
        Resume.objects.all().delete()

        self.client.login(username='admin', password='admin')
        response = self.client.get(self.resume_create, {})

        received = response.request['REQUEST_METHOD']
        expected = 'GET'

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/resume/create.html')
        self.assertEqual(received, expected)

    def test_create_resume_notValid_creating(self):
        '''Форма создания резюме не проходит резюме'''
        Resume.objects.all().delete()

        self.client.login(username='admin', password='admin')
        response = self.client.post(self.resume_create, {})

        received = response.context['status']
        expected = 'creating'

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/resume/create.html')
        self.assertEqual(received, expected)

    def test_create_resume_creating_ready(self):
        '''Создается валидное резюме'''
        Resume.objects.all().delete()

        self.client.login(username='admin', password='admin')
        response = self.client.post(self.resume_create, {'first_name': 'admin',
                                                         'last_name': 'admin',
                                                         'email': 'a@mail.ru',
                                                         'phone': '123456789',
                                                         'description': 'any'})

        received = response.context['status']
        expected = 'ready'

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/resume/create.html')
        self.assertEqual(received, expected)
#-----------------------------------------------------------------------------------------------

#----create_auto_post---------------------------------------------------------------------------
    @patch('utils.parser_dev_by.ParserDevBy.get_links', return_value=[])
    def test_create_auto_post_not_links_str(self, ass):
        '''когда не найдено ни одной ссылки'''
        self.client.login(username='admin', password='admin')
        response = self.client.get(self.url_create_auto_post)
        received = response.context['status']
        expected = 'Вакансии не обновлены'
        print(received)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/post/test.html')
        self.assertEqual(received, expected)

    @patch('utils.parser_dev_by.ParserDevBy.get_links', return_value=[2,])
    def test_create_auto_post_error_str(self, ass):
        '''когда функция возвращается при вызове ошибки(try: except)'''
        self.client.login(username='admin', password='admin')
        response = self.client.get(self.url_create_auto_post)
        received = response.context['status']
        expected = 'Обновление прервано'

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/post/test.html')
        self.assertEqual(received, expected)

    @patch('utils.parser_dev_by.ParserDevBy.get_links', return_value=[2, ])
    @patch('utils.parser_dev_by.ParserDevBy.get_info_work', return_value={'Агент':{'email': 'ad@mail.ru'}})
    @patch('utils.parser_dev_by.ParserDevBy.get_info_user', return_value={'email': 'ad@mail.ru'})
    def test_create_auto_post_notAddNewUser_str(self, ass, s, a):
        '''когда находится действующий пользователь'''
        self.client.login(username='admin', password='admin')
        response = self.client.get(self.url_create_auto_post)
        received = response.context['agent']
        expected = 'Найдены пользователи'

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/post/test.html')
        self.assertEqual(received, expected)

    @patch('utils.parser_dev_by.ParserDevBy.get_links', return_value=[2, ])
    @patch('utils.parser_dev_by.ParserDevBy.get_info_work', return_value={
         'link': 'https://www.test.by',
         'Название': 'test_title',
         'Специализация': '',
         'Уровень': '',
         'Опыт': '',
         'Уровень английского': '',
         'Зарплата': '',
         'Город': '',
         'Режим работы': '',
         'Размер команды': '',
         'Размер компании': 20,
         'Возможна удалённая работа': True,
         'Описание': 'ad@mail.ru',
         'Тэги': [],
         'Агент':{'first_name': 'test_first_name',
                 'last_name': 'test_title',
                 'username': 'test_username',
                 'email': 'asm@mail.ru',
                 }})
    @patch('utils.parser_dev_by.ParserDevBy.get_info_user', return_value={
                 'first_name': 'test_first_name',
                 'last_name': 'test_title',
                 'username': 'test_username',
                 'email': 'asm@mail.ru',})
    def test_create_auto_post_addNewUser_str(self, ass, s, a):
        '''когда создается новый пользователь без добавления и вакансия без тегов'''
        self.client.login(username='admin', password='admin')
        response = self.client.get(self.url_create_auto_post)
        received = response.context['agent'] + ';' + response.context['status']
        expected = 'Добавлены новые пользователи;Вакансии обновлены'

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/post/test.html')
        self.assertEqual(received, expected)

    @patch('utils.parser_dev_by.ParserDevBy.get_links', return_value=[2, ])
    @patch('utils.parser_dev_by.ParserDevBy.get_info_work', return_value={
         'link': 'https://www.test.by',
         'Название': 'test_title',
         'Специализация': '',
         'Уровень': '',
         'Опыт': '',
         'Уровень английского': '',
         'Зарплата': '',
         'Город': '',
         'Режим работы': '',
         'Размер команды': '',
         'Размер компании': 20,
         'Возможна удалённая работа': True,
         'Описание': 'ad@mail.ru',
         'Тэги': ['tag1', 'tag2', 'tag3'],
         'Агент':{'first_name': 'test_first_name',
                 'last_name': 'test_title',
                 'username': 'test_username',
                 'email': 'asm@mail.ru',
                 }})
    @patch('utils.parser_dev_by.ParserDevBy.get_info_user', return_value={
                 'first_name': 'test_first_name',
                 'last_name': 'test_title',
                 'username': 'test_username',
                 'email': 'asm@mail.ru',})
    def test_create_auto_post_withTags_str(self, ass, s, a):
        '''когда создается новый пользователь без добавления и вакансия без тегов'''
        self.client.login(username='admin', password='admin')
        response = self.client.get(self.url_create_auto_post)
        received = response.context['agent'] + ';' + response.context['status']
        expected = 'Добавлены новые пользователи;Вакансии обновлены'

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work/post/test.html')
        self.assertEqual(received, expected)
#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    TestViews.run()
