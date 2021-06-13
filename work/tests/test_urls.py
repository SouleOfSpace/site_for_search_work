from django.test import SimpleTestCase
from django.urls import reverse, resolve
from work.views import post_list, post_list_by_search, post_detail, create_auto_post, create_post, newswork_detail, create_resume

class TestUrls(SimpleTestCase):
    '''pass'''
    def test_post_list_is_resolved(self):
        '''Возвращает страницу со списком вакансий'''
        url = reverse('work:post_list')
        self.assertEqual(resolve(url).func, post_list)

    def test_post_list_by_tag_resolved(self):
        '''Возвращает страницу со списком вакансий по тегу'''
        url = reverse('work:post_list_by_tags', args=['tag'])
        self.assertEqual(resolve(url).func, post_list)

    def test_post_list_by_search_resolved(self):
        '''Возвращает страницу со списком вакансий по поисковому слову'''
        url = reverse('work:search')
        self.assertEqual(resolve(url).func, post_list_by_search)

    def test_post_detail_resolved(self):
        '''Возвращает страницу с детальным описание вакансии'''
        url = reverse('work:post_detail', args=['2021', '4', '14', 'slug', '1'])
        self.assertEqual(resolve(url).func, post_detail)

    def test_post_create_resolved(self):
        '''Возвращает страницу с созданием вакансии'''
        url = reverse('work:post_create')
        self.assertEqual(resolve(url).func, create_post)

    def test_post_create_auto_resolved(self):
        '''Возвращает страницу с автоматическим созданием вакансий'''
        url = reverse('work:post_create_auto')
        self.assertEqual(resolve(url).func, create_auto_post)

    def test_news_detail_resolved(self):
        '''Возвращает страницу с детальным описанием новости'''
        url = reverse('work:news_detail', args=['slug', '1'])
        self.assertEqual(resolve(url).func, newswork_detail)

    def test_create_resume_resolved(self):
        '''Возвращает страницу с созданием резюме'''
        url = reverse('work:resume_create', args=['1',])
        self.assertEqual(resolve(url).func, create_resume)

if __name__ == '__main__':
    TestUrls.run()
