
'''
this file  contain tests
'''

from unittest import TestCase
from post import Post

class PostTest(TestCase):
    '''
    Test for class Post
    '''
    def test_create_post(self):
        '''
        test for creating object
        '''
        p_1 = Post('Test', 'Test Content')
        self.assertEqual('Test', p_1.title)
        self.assertEqual('Test Content', p_1.content)

    def test_json(self):
        '''
        Test for json method from class Post
        '''
        p_1 = Post('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}

        self.assertDictEqual(expected, p_1.json())
    def test_obj_instance(self):
        '''
        Test if object is instane of class Post
        '''
        p_1 = Post('Test', 'Test Content')

        self.assertIsInstance(p_1, Post)

    def test_str(self):
        '''
        Test for method __str__ on object
        '''
        p_1 = Post('Test', 'Test Content')
        self.assertEqual(p_1.__str__(), f"Title: {p_1.title}, Content: {p_1.content}")

    def test_repr(self):
        '''
        Test for method __repr__ on object
        '''
        p_1 = Post('Test', 'Test Content')
        self.assertEqual(p_1.__repr__(), f",Post('{p_1.title}'', '{p_1.content}')")
