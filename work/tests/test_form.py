from django.test import TestCase, Client
from work import forms
from django.contrib.auth.models import User

class TestForms(TestCase):

    def test_post_form_valid_True(self):
        '''форма, прошедшая валидацию'''
        form = forms.PostForm(data={
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
            'tags': 'python'
        })

        self.assertTrue(form.is_valid())

    def test_post_form_notValid_False(self):
        '''форма, не прошедшая валидацию'''
        form = forms.PostForm(data={})

        self.assertFalse(form.is_valid())

    def test_advencedSearchForm_valid_True(self):
        '''форма, прошедшая валидацию'''
        form = forms.AdvencedSearchForm(data={
            'title': 'test',
            'specialization': '',
            'level': '',
            'experience': '',
            'level_english': '',
            'salary': '',
            'city': '',
            'mode_work': '',
            'size_company': 'None',
            'talework': True,
        })

        self.assertTrue(form.is_valid())

    def test_advencedSearchForm_notValid_False(self):
        '''форма, не прошедшая валидацию'''
        form = forms.AdvencedSearchForm(data={'title': '12345678909898'
                                                       '76867684567777'})

        self.assertFalse(form.is_valid())

    def test_searchForm_valid_True(self):
        '''форма, прошедшая валидацию'''
        form = forms.SearchForm(data={
            'query': 'Test',
        })

        self.assertTrue(form.is_valid())

    def test_searchForm_notValid_False(self):
        '''форма, не прошедшая валидацию'''
        form = forms.SearchForm(data={})

        self.assertFalse(form.is_valid())

    def test_resumeForm_valid_True(self):
        '''форма, прошедшая валидацию'''
        form = forms.ResumeForm(data={
            'first_name': 'test',
            'last_name': 'test',
            'email': 's@mail.ru',
            'phone': '123456789',
            'description': 'test',
        })

        self.assertTrue(form.is_valid())

    def test_resumeForm_notValid_False(self):
        '''форма, не прошедшая валидацию'''
        form = forms.ResumeForm(data={})

        self.assertFalse(form.is_valid())

if __name__ == '__main__':
    TestCase.run()
