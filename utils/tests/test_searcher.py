import unittest
from utils import searcher

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
        self.destroer = searcher.Searcher()
        print('\nSet up for    [' + self.shortDescription() + ']')

    def tearDown(self):
        '''pass'''
        print('Tear Down for [' + self.shortDescription() + ']\n')

#-------------------------TESTS-------------------------------------------
    # @unittest.skip("test_get_destroed_tracker_equality_python_django_java_dev skipping")
    def test_get_destroed_tracker_equality_python_django_java_dev(self):
        '''test_get_destroed_tracker_equality_python_django_java_dev
            проверяет работу программы при стандартном запросе который разделиться на несколько элементов
        '''
        value = 'python;Django Java,Dev'
        actual_result = self.destroer.get_destroed_requests(value)
        expected_result = ['python', 'Django', 'Java', 'Dev']
        self.assertEqual(actual_result, expected_result)

    # @unittest.skip("test_get_destroed_tracker_valid_nullArray skipping")
    def test_get_destroed_tracker_valid_nullArray(self):
        '''test_get_destroed_tracker_valid_nullArray
            проверяет работу программы при пустом запросе
        '''
        value = ''
        actual_result = self.destroer.get_destroed_requests(value)
        expected_result = ['']
        self.assertEqual(actual_result, expected_result)

    # @unittest.skip("test__get_destroed_tracker_equality_python_django_java_dev skipping")
    def test_get_destroed_tracker_equalityPythonDjangoJavaDev(self):
        '''test_get_destroed_tracker_equality_python_django_java_dev
            проверяет работу программы при запросе, который не будет разделяться
        '''
        value = 'pythonDjangoJavaDev'
        actual_result = self.destroer.get_destroed_requests(value)
        expected_result = ['pythonDjangoJavaDev']
        self.assertEqual(actual_result, expected_result)

    # @unittest.skip("test__get_destroed_tracker_equality_python_django_java_dev skipping")
    def test_get_destroed_tracker_equalityBariers(self):
        '''test_get_destroed_tracker_equality_python_django_java_dev
            проверяет работу программы при запросе, который который состоит из разделителей
        '''
        value = ';, '
        actual_result = self.destroer.get_destroed_requests(value)
        expected_result = ['']
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
