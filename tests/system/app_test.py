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

    Args:
        TestCase ([type]): this is unittest module
    """

    def test_menu_input(self):
        """
        This will test the argument for input function
        from the menu function
        """

        with patch("builtins.input") as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        """
        This will test if the menu function calls
        the print_blogs function
        """

        with patch("app.print_blogs") as mocked_print_blogs:
            with patch("builtins.input"):
                app.menu()
                mocked_print_blogs.assert_called_with()

    def test_print_blogs(self):
        """
        This is test for blog printing. In this example
        the "print_blog" function is not returning anything
        so the patch needs to be used on the print function
        """

        blog = Blog("Test title", "Test author")
        app.blogs.update({"FirstBlog": blog})

        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("- Title: Test title, Author: Test author (0 posts)")

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
        blog = Blog("Test title", "Test author")
        app.blogs.update({"Test title": blog})

        with patch('builtins.input', return_value='Test title'):
            with patch('app.print_posts') as mocked_print_posts:
                app.read_blog()
                mocked_print_posts.assert_called_with(blog)

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