from utils.parser_dev_by import ParserDevBy
from bs4 import BeautifulSoup
import unittest

class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''Set up for Class'''
        print('SetUpClass\n==========\n')

    @classmethod
    def tearDownClass(cls):
        '''Tear Down for Class'''
        # print(cls.countTestCases())
        print('==========\nTearDownClass\n')
        cls.skipTest('skipped', reason='fdgf')

    def setUp(self):
        '''Set Up'''
        self.parser = ParserDevBy()
        print('\nSet up for    [' + self.shortDescription() + ']')

    def tearDown(self):
        '''pass'''
        print('Tear Down for [' + self.shortDescription() + ']\n')

# test_check_connect----------------------------------------------------------------
#     @unittest.skip("test_check_connect_check_on_true skipping")
    def test_check_connection_valid_true(self):
        '''test_check_connect_check_on_true
        Должен возвратить TRue если есть интернет соеденение
        '''
        expected_result = self.parser.check_connect()
        self.assertTrue(expected_result)

    @unittest.skip("test_check_connection_check_off_false skipping")
    def test_check_connection_valid_false(self):
        '''test_check_connect_check_off_false
        Должен возвратить False если нет интернет соеденения
        '''
        actual_result = self.parser.check_connect()
        self.assertFalse(actual_result)
#------------------------------------------------------------------------------------------------------------

# test_create_link----------------------------------------------------------------
#     @unittest.skip("test_create_link_equality_httpsJobsDevByMyStr skipping")
    def test_create_link_equality_httpsJobsDevByMyStr(self):
        '''test_create_link_equality_httpsJobsDevByMyStr
        Должен возвратить правильную ссылку https://jobs.dev.by/myStr'''
        actual_result = self.parser.create_link('/myStr')
        expected_result = 'https://jobs.dev.by/myStr'
        self.assertEqual(actual_result, expected_result)
# ------------------------------------------------------------------------------------------------------------

# test_get_links----------------------------------------------------------------
#     @unittest.skip("test_create_link_equality_httpsJobsDevByMyStr skipping")
    def test_get_links_valid_TypeError(self):
        '''Должен возвратить ошибку когда аргумент не равен str'''
        value = 1
        actual_result = self.parser.get_links()
        expected_result = TypeError
        # self.assertEqual(actual_result, expected_result)
        self.assertRaises(expected_result, actual_result, value)

    @unittest.skip("test_get_links_validConnect_errorMsg skipping")
    def test_get_links_validConnect_errorMsg(self):
        '''test_get_links_validConnect_errorMsg запускать отдельно от test_scrape_dev_by_checkConnect_True
        Должен возвратить массив длиной сообщение, если нет интернет соеденение
        '''
        actual_result = self.parser.get_links()
        expected_result = 'Отсутствует интернет подключение'
        self.assertEqual(actual_result, expected_result)

    # @unittest.skip("test_get_links_searchedLinks_True skipping")
    def test_get_links_searchedLinks_True(self):
        '''test_get_links_searchClass_noneArr
        Должен возвратить массив больше 0, при правильном аргументе функции (название нужного класса)
        и интернет соеденением
        '''
        actual_result = bool(len(self.parser.get_links()))
        self.assertTrue(actual_result)

    # @unittest.skip("test_get_links_SearchedLinks_False skipping")
    def test_get_links_Searchedlinks_False(self):
        '''test_get_links_SearchClass_False
        Должен возвратить пустой массив, при не правильном аргументе функции (название нужного класса)
        и интернет соеденением
        '''
        actual_result = self.parser.get_links('adfadsf')
        expected_result = []
        self.assertEqual(actual_result, expected_result)
#----------------------------------------------------------------------------------------------

#----get_info_work-----------------------------------------------------------------------------
    # @unittest.skip("test_create_link_equality_httpsJobsDevByMyStr skipping")
    def test_get_info_work_valid_True(self):
        '''При правильно заданной ссылке должен возвратить словарь, а это равно значению True'''
        actual_result = bool(self.parser.get_info_work('https://jobs.dev.by/vacancies/22770'))
        self.assertTrue(actual_result)

    # @unittest.skip("test_create_link_equality_httpsJobsDevByMyStr skipping")
    def test_get_info_work_valid_Raises(self):
        '''При не правильно заданной ссылке должен возвратить ошибку'''
        self.assertRaises(AttributeError, self.parser.get_info_work, 'https://google.com')
#----------------------------------------------------------------------------------------------

#---get_info_user------------------------------------------------------------------------------
    # @unittest.skip("test_get_info_user skipping")
    def test_get_info_user_valid_dict(self):
        '''Должен возвратить словарь из данных пользователя расположенного по заданной ссылке'''
        actual_result = self.parser.get_info_user('https://id.dev.by/users/evgeniya-babitskaya')
        expected_result = {'first_name': 'Evgeniya',
                           'last_name': 'Babitskaya',
                           'username': 'evgeniya-babitskaya',
                           'email': 'evgeniya.babitskaya@expcapital.com'
                            }
        self.assertEqual(actual_result, expected_result)
#----------------------------------------------------------------------------------------------

#----test utils for get_info_worl-----------------------------------------------------------------------------------------
    # @unittest.skip("test_get_vacancy_tags_found_True skipping")
    def test_get_vacancy_tags_found_True(self):
        '''Должен возвратить не пустую строку(а это True), когда теги найдены'''
        actual_result = bool(self.parser.get_vacancy_tags('https://jobs.dev.by/vacancies/20326'))
        self.assertTrue(actual_result)

    # @unittest.skip("test_create_link_equality_httpsJobsDevByMyStr skipping")
    def test_get_vacancy_tags_found_False(self):
        '''Должен возвратить пустую строку(а это False), когда теги не найдены'''
        actual_result = bool(self.parser.get_vacancy_tags('https://google.com'))
        self.assertFalse(actual_result)

    # @unittest.skip("test_create_link_equality_httpsJobsDevByMyStr skipping")
    def test_get_vacancy_description_found_True(self):
        '''Должен возвратить не пустую строку(а это True), когда описание найдено'''
        actual_result = bool(self.parser.get_description('https://jobs.dev.by/vacancies/20326'))
        self.assertTrue(actual_result)

    # @unittest.skip("test_create_link_equality_httpsJobsDevByMyStr skipping")
    def test_get_vacancy_description_found_False(self):
        '''Должен возвратить не пустую строку(а это False), когда описание не найдено'''
        actual_result = bool(self.parser.get_description('https://google.com'))
        self.assertFalse(actual_result)

    # @unittest.skip("test_create_link_equality_httpsJobsDevByMyStr skipping")
    def test_get_talework_have_True(self):
        '''Если значение словаря не равно пустой строке, то возвращаем True'''
        actual_result = self.parser.get_talework({'Возможна удалённая работа':'1',})
        self.assertTrue(actual_result)

    # @unittest.skip("test_create_link_equality_httpsJobsDevByMyStr skipping")
    def test_get_talework_haveNot_False(self):
        '''Если значение словаря равно пустой строке, то возвращаем False'''
        actual_result = self.parser.get_talework({'Возможна удалённая работа': '',})
        self.assertFalse(actual_result)
#--------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()
