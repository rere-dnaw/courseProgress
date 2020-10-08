'''
This file contain a Blog class
'''
from post import Post

class Blog:
    '''
    This is a blog class
    '''
    def __init__(self, title, author):
        '''
        Initialize method
        '''
        self.title = title
        self.author = author
        self.posts = []

    def __str__(self):
        '''
        This is what the print method will return
        '''
        return "Title: {}, Author: {} ({} post{})".format(self.title,
                                                          self.author,
                                                          len(self.posts),
                                                          's' if len(self.posts) != 1 else '')

    def __repr__(self):
        '''
        String representation of the class
        '''
        return "{} by {} ({} post{})".format(self.title,
                                             self.author,
                                             len(self.posts),
                                             's' if len(self.posts) != 1 else '')

    def json(self):
        '''
        This method will return a dict for object
        '''
        return {
            'Title': self.title,
            'Author': self.author,
            'Posts': [post.json() for post in self.posts]
        }

    def create_post(self, title, content):
        '''
        This method will create post and add it into posts list
        '''
        self.posts.append(Post(title, content))
