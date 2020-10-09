"""
This is an app
"""

from blog import Blog

MENU_PROMPT = '''Enter "c  to create blog,
              "l" to list blogs, 
              "r" to read the blog, 
              "p" to create a post or 
              "q" to quit:'''

CREATE_BLOG_TITLE_PROMPT = 'Enter the blog title: '
CREATE_BLOG_AUTHOR_PROMPT = 'Enter the author name: '
READ_BLOG_PROMPT = "What's a blog title?"

POST_TEMPLATE = """
--- {} ---

{}

"""

blogs = dict()  # blog_name: Blog object


def menu():
    """
    Shows the user the available blogs
    Let the user make a choice
    Do something with the choice
    Exit.
    """

    print_blogs()
    selection = input(MENU_PROMPT)

    while selection != 'q':
        if selection == 'c':
            create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            read_blog()
        elif selection == 'p':
            create_post()
        selection = input(MENU_PROMPT)


def create_blog():
    """
    This function will create a new blog.
    """
    title = input(CREATE_BLOG_TITLE_PROMPT)
    author = input(CREATE_BLOG_AUTHOR_PROMPT)
    blog = Blog(title, author)
    blogs.update({title: blog})


def read_blog():
    """
    This function will read the blog
    """
    blog_title = input(READ_BLOG_PROMPT)

    print_posts(blogs[blog_title])


def print_posts(blog):
    """
    This function will print all posts from the blog
    Args:
        blog (Blog): This is a blog object
    """
    for post in blog.posts:
        print_post(post)


def print_post(post):
    """
    This function will print a single post

    Args:
        post (Post): This a post
    """
    print(POST_TEMPLATE.format(post.title, post.content))


def create_post():
    """
    this function will create a post
    """
    blog_name = input(READ_BLOG_PROMPT)

    for key, blog in blogs.items():
        if key == blog_name:
            blog.create_post('Post title', 'Post content')


def print_blogs():
    """
    Print the available blogs
    """

    for key, blog in blogs.items():
        print('- {}'.format(blog))
