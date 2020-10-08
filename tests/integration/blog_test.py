'''
This file sontain unit tests for blog.py file
'''

from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    '''
    Unit tests for blog class
    '''
    def test_create_post(self):
        '''
        Unit test for create post method
        '''
        b_1 = Blog('Test title', 'Test author')
        b_1.create_post('Test Post', 'Test Content')

        self.assertEqual(len(b_1.posts), 1)
        self.assertEqual(b_1.posts[0].title, 'Test Post')
        self.assertEqual(b_1.posts[0].content, 'Test Content')

    def test_json(self):
        '''
        Unit test for json method
        '''
        b_1 = Blog('Test title', 'Test author')
        b_1.create_post('Test Post', 'Test Content')

        expected = {'Title': 'Test title',
                    'Author': 'Test author',
                    'Posts': [post.json() for post in b_1.posts],}

        self.assertDictEqual(b_1.json(), expected)

    def test_json_no_post(self):
        '''
        Unit test for json method when no posts
        '''
        b_1 = Blog('Test title', 'Test author')

        expected = {'Title': 'Test title',
                    'Author': 'Test author',
                    'Posts': [post.json() for post in b_1.posts],}

        self.assertDictEqual(b_1.json(), expected)
