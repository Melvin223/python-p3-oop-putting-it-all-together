#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        '''Initialize the book with a title and page count.'''
        self.title = title
        self._page_count = None
        self.page_count = page_count

    @property
    def page_count(self):
        '''Get the page count of the book.'''
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        '''Set the page count of the book, ensuring it's an integer.'''
        if isinstance(value, int):
             self._page_count = value
        else:
            print("page_count must be an integer")
            self._page_count = None

    def turn_page(self):
        '''Simulate turning a page of the book.'''
        print("Flipping the page...wow, you read fast!")
    pass
    
        