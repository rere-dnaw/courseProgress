"""
This is system test for app.py file
"""

from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog


class AppTest(TestCase):
    """
    This class will test all the funstions from the app.py file

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
