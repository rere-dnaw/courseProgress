"""
This file contain unit tests for blog.py file
"""

from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    """
    Unit tests for blog class
    """

    def test_create_blog(self):
        """
        This is test for creating new objects
        """
        b_1 = Blog('Test title', 'Test author')
        self.assertEqual(b_1.title, 'Test title')
        self.assertEqual(b_1.author, 'Test author')
        self.assertListEqual(b_1.posts, [])
        self.assertEqual(len(b_1.posts), len([]))

    def test_repr(self):
        """
        Test for __repr__ method
        """
        b_1 = Blog('Test title', 'Test author')
        b_1.posts = ['One']

        b_2 = Blog('Test title2', 'Test author2')
        b_2.posts = ['One', 'Two']

        self.assertEqual(b_1.__repr__(), "Test title by Test author (1 post)")
        self.assertEqual(b_2.__repr__(), "Test title2 by Test author2 (2 posts)")

    def test_str(self):
        """
        This is test for string which is return by print method
        """
        b_1 = Blog('Test title', 'Test author')
        b_1.posts = ['One']

        b_2 = Blog('Test title2', 'Test author2')
        b_2.posts = ['One', 'Two']
        print(b_1)
        print(b_2)

        self.assertEqual(b_1.__str__(), "Title: Test title, Author: Test author (1 post)")
        self.assertEqual(b_2.__str__(), "Title: Test title2, Author: Test author2 (2 posts)")
