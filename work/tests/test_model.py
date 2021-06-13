from django.test import TestCase, Client
from django.contrib.auth.models import User

from work.models import Post, Newswork, Resume

# Create your tests here.

class PostModelTest(TestCase):

    def setUp(self):
        #Set up non-modified objects used by all test methods
        self.client = Client()
        self.user_admin = User.objects.create(username='admin', password='admin', email='ad@mail.ru',
                                                   first_name='sasha',
                                                   last_name='volosevich')
        self.client.login(username='admin', password='admin')

        self.post = Post.objects.create(link='https://www.test.ru',
                                        title='test',
                                        talework=True,
                                        agent=self.user_admin,
                                        size_company=20,
                                        ).save()

        Newswork.objects.create(agent=self.user_admin,
                                title='test',
                                body='sss').save()

# start test get_absolute_url-------------------------------------------------------------------------------------------
    def test_postGet_absolute_url_url(self):
        '''Возвращает страницу с дельным описание вакансии'''
        post = Post.objects.first()
        field_url = post.get_absolute_url()
        self.assertEquals(field_url, '/works/2021/6/13/test/1/')

    def test_newsworkGet_absolute_url_url(self):
        '''Возвращает страницу с дельным описанием новости'''
        post = Newswork.objects.last()
        field_url = post.get_absolute_url()
        self.assertEquals(field_url, '/works/news/test/1/')
# finish test get_absolute_url------------------------------------------------------------------------------------------

# start test slug--------------------------------------------------------------------------------------------------------
    def test_postSave_slug(self):
        '''При сохранении модели автоматически создает slug'''
        post = Post.objects.get(id=1)

        received = post.slug
        expected = 'test'

        self.assertEqual(received, expected)

    def test_newsworkSave_slug(self):
        '''При сохранении модели автоматически создает slug'''
        new = Newswork.objects.get(id=1)
        received = new.slug
        expected = 'test'

        self.assertEqual(received, expected)

    def test_resumeSave_slug(self):
        '''При сохранении модели автоматически создает slug'''
        Resume.objects.create(post_id=1, post=self.post, first_name='test', last_name='test',
                              email='test@mail.ru', phone='12345678'
                              ).save()

        res = Resume.objects.get(id=1)
        received = res.slug
        expected = 'test-test'

        self.assertEqual(received, expected)
# finish test slug

if __name__ == '__main__':
    PostModelTest().run()
