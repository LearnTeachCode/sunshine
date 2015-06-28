'''
Created on June 20, 2015
Candidate Object is the speaking legislator
Candidate holds a list of messages (spoken word)

06-27-15
To-do: fix error from text
change to proper object syntax

@author: 
    Sina Tuy
    Kiron Roy
    Richard Chen
    Kendra Branton
    Hong Luu
'''
from Message import *

class CandidateObject():
    def __init__(self, id, first_name, last_name, party):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.party = party
        self.message_list = []
        
    def addMessage(self, text, date, headline):
        message = MessageObject(text, headline, date)
        self.message_list.append(message)
        
    def getMessage(self):
        messages = ''
        for message in self.message_list:
            messages += "\ntitle: " + message.title
            messages += "\ndate: " + message.date
#             messages += "\ntext: " + Message.text
        return messages
            