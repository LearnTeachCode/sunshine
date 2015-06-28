'''
Created on June 25, 2015

Holds the message of a speaking legislator

06-28-15
To-do: change to proper object syntax

@author: 
    Sina Tuy
    Kiron Roy
    Richard Chen
    Kendra Branton
    Hong Luu
'''


class MessageObject():
    def __init__(self, text, title, date):
        self.text = text
        self.title = title
        self.date = date