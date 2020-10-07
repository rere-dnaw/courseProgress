
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
