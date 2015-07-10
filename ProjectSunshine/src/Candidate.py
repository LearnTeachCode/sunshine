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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

class CandidateObject():
    def __init__(self, candidate_id, first_name, last_name, party):
        self.id = candidate_id
        self.first_name = first_name
        self.last_name = last_name
        self.party = party
        self.message_list = []
        self.word_list = {}
        self.top_words = {}
        
    def addMessage(self, text, date, headline):
        message = MessageObject(text, headline, date)
        self.message_list.append(message)
        self.filterWords(text)
        
    def filterWords(self, text):
        for line in text:
            word = ''
            for letter in line:
                # ignore if letter contains comma or space or parenthesis
                if letter != ',' and letter != ' ' and letter != '(' and letter != ')':
                    if letter == '.':
                        # do not ignore period if it's Mr. or Mrs. or Ms.
                        if word == "Mr" or word == "Mrs" or word == "Ms": 
                            word += letter
                        # do not ignore period if it's single letters
                        elif len(word) == 1:
                            word += letter
                    else: 
                        word += letter
                if letter == ' ' or letter == '\n' or letter == '.':
                    # handles issue of word containing only a blank space
                    if len(word) > 0:
                        # do not include 's in our words
                        if word.__contains__("'s"):
                            temp_word = word.split("'")
                            word = temp_word[0]
#                         print (word)
                        self.hashWord(word.lower())
                    word = ''
        
    def hashWord(self, word):
        if self.word_list.has_key(word) == False:
            self.word_list[word] = 1
        else:
            number = self.word_list[word] + 1
            self.word_list[word] = number

    def getMessage(self):
        messages = ''
        for message in self.message_list:
            messages += "\ntitle: " + message.title
            messages += "\ndate: " + message.date
            messages += "\ntext: "
            for text in message.text:
                messages += "\n\t"
                messages += text
        return messages
            
    def printLSA(self):
        corpus = []
        for message in self.message_list:
            corpus += message.text
#         for message in self.message_list:
#             for text in message.text:
#                 corpus.append(text)
        #tfidf stuff
        vectorizer = TfidfVectorizer(min_df=1, stop_words='english')
        X = vectorizer.fit_transform(corpus)
        idf = vectorizer.idf_
        #lsa stuff
        lsa = TruncatedSVD(n_components=27, n_iter=100)
        lsa.fit(X)
    
        print dict(zip(vectorizer.get_feature_names(), idf))
        print ""
        
        #print related concepts
        terms = vectorizer.get_feature_names()
        for i, comp in enumerate(lsa.components_): 
            termsInComp = zip (terms,comp)
            sortedTerms =  sorted(termsInComp, key=lambda x: x[1], reverse=True) [:10]
            print "Concept %d:" % i
            for term in sortedTerms:
                print term[0]
            print " "
        
        #print sorted stuff to see    
        v = sorted(zip(vectorizer.get_feature_names(), idf), key=lambda x:x[1])
        print v
        print "\n\n"
            
    def printWords(self):
        for word in self.word_list:
            message = ''
            message += word
            message += ', '
            message += str(self.word_list[word])
            print (message)
            
    def setTopWords(self):
        top1_word = ''
        top2_word = ''
        top3_word = ''
        top4_word = ''
        top5_word = ''
        top6_word = ''
        top7_word = ''
        top8_word = ''
        top9_word = ''
        top10_word = ''
        top1_count = 0
        top2_count = 0
        top3_count = 0
        top4_count = 0
        top5_count = 0
        top6_count = 0
        top7_count = 0
        top8_count = 0
        top9_count = 0
        top10_count = 0
        for word in self.word_list:
            if top1_count < self.word_list[word]:
                top1_count = self.word_list[word]
                top1_word = word

            elif top2_count < self.word_list[word]:
                top2_count = self.word_list[word]
                top2_word = word

            elif top3_count < self.word_list[word]:
                top3_count = self.word_list[word]
                top3_word = word

            elif top4_count < self.word_list[word]:
                top4_count = self.word_list[word]
                top4_word = word

            elif top5_count < self.word_list[word]:
                top5_count = self.word_list[word]
                top5_word = word

            elif top6_count < self.word_list[word]:
                top6_count = self.word_list[word]
                top6_word = word

            elif top7_count < self.word_list[word]:
                top7_count = self.word_list[word]
                top7_word = word

            elif top8_count < self.word_list[word]:
                top8_count = self.word_list[word]
                top8_word = word

            elif top9_count < self.word_list[word]:
                top9_count = self.word_list[word]
                top9_word = word

            elif top10_count < self.word_list[word]:
                top10_count = self.word_list[word]
                top10_word = word

        self.top_words[top1_word] = top1_count
        self.top_words[top2_word] = top2_count
        self.top_words[top3_word] = top3_count
        self.top_words[top4_word] = top4_count
        self.top_words[top5_word] = top5_count
        self.top_words[top6_word] = top6_count
        self.top_words[top7_word] = top7_count
        self.top_words[top8_word] = top8_count
        self.top_words[top9_word] = top9_count
        self.top_words[top10_word] = top10_count

    def getTopWords(self):
        return self.top_words