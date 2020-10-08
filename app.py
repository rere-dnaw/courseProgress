"""
This is an app
"""

MENU_PROMPT = '''Enter "c  to create blog,
              "l" to list blogs, 
              "r" to read the blog, 
              "p" to create a post or 
              "q" to quit:'''

blogs = dict() # blog_name: Blog object


def menu():
    """
    Shows the user the available blogs
    Let the user make a choice
    Do swomething with the choice
    Exit.
    """

    selection = input(MENU_PROMPT)
    print_blogs()

def print_blogs():
    """
    Print the avaliable blogs
    """

    for key, blog in blogs.items():
        print('- {}'.format(blog))
    