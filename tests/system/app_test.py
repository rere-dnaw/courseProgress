"""
This is system test for app.py file
"""

from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    """
    This class will test all the functions from the app.py file
    """

    def setUp(self):
        """
        This method will be called before each test
        """
        self.blog = Blog("Test title", "Test author")
        app.blogs.update({"FirstBlog": self.blog})

    def test_menu_calls_print_blogs(self):
        """
        This will test if the menu function calls
        the print_blogs function
        """

        with patch("app.print_blogs") as mocked_print_blogs:
            with patch("builtins.input", return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called_with()

    def test_print_blogs(self):
        """
        This is test for blog printing. In this example
        the "print_blog" function is not returning anything
        so the patch needs to be used on the print function
        """

        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("- Title: Test, Author: Test Author (0 posts)")

        # this works only when func return something
        # See: https://www.youtube.com/watch?v=WFRljVPHrkE
        # with patch("app.print_blogs", return_value =
        #                           "- Title: Test title, Author: Test author (0 posts)"):
        #     actual_result = app.print_blogs()

        # expected_result = "- Title: Test title, Author: Test author (0 posts)"
        # self.assertEqual(actual_result, expected_result)

    def test_create_blog(self):
        """
        This is test for create_blog function
        """

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_read_blog(self):
        """
        This is test for read_blog function
        """

        with patch('builtins.input', return_value='FirstBlog'):
            with patch('app.print_posts') as mocked_print_posts:
                app.read_blog()
                mocked_print_posts.assert_called_with(self.blog)

    def test_print_posts(self):
        """
        This is a test for print_posts function
        """
        blog = Blog("My days", "RW")
        blog.create_post('Post 1', 'This is my first post')
        blog.create_post('Post 2', 'This is my second post')
        app.blogs.update({"My days": blog})

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[1])

    def test_print_post(self):
        """
        This is a test for print_post function
        """
        post = Post('Post1', 'This is my first post')
        expected_print = """
--- Post1 ---

This is my first post

"""

        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)

    def test_create_post(self):
        """
        This is a test for create post function
        """

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('FirstBlog', 'My post title', 'My post content')
            app.create_post()

            self.assertEqual(self.blog.posts[0].title, 'My post title')
            self.assertEqual(self.blog.posts[0].content, 'My post content')

    def test_menu_selection_c(self):
        """
        This is a test for selection option 'c'
        """

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'The blog title', "The blog's author", 'q')
            app.menu()
            self.assertIsNotNone(app.blogs['The blog title'])

    def test_menu_selection_c(self):
        """
        This is a test for selection option 'l'
        """

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('l', 'q')
            with patch('app.print_blogs') as mocked_print_blogs:
                app.menu()
                mocked_print_blogs.assert_called()

    def test_menu_selection_r(self):
        """
        This is a test for selection option 'r'
        """

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('r', 'FirstBlog', 'q')
            with patch('app.read_blog') as mocked_read_blog:
                app.menu()
                mocked_read_blog.assert_called()

    def test_menu_selection_p(self):
        """
        This method will test an option "p" from
        the selection menu
        """

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('p', 'FirstBlog', 'Post titleX', 'Post contentX', 'q')
            with patch('app.create_post') as mocked_create_post:
                app.menu()
                mocked_create_post.assert_called()


