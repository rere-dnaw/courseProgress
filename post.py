'''
This file contain the Post class
'''

class Post:
    '''
    The post class
    '''
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"Title: {self.title}, Content: {self.content}"

    def __repr__(self):
        return f",Post('{self.title}'', '{self.content}')"

    def json(self):
        '''
        This method return dict object
        '''
        return {
            'title': self.title,
            'content': self.content,
        }
