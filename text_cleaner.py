from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import re 

class text_cleaner(object):

    def __init__(self):
        pass
    
    def clean_text_dict(self, raw_text_dict):
        #This function takes a dictionary of a dictionary as an input
        #This function performs the following operations:
        #1. Escapes HTML characters
        #3. Remove stop words
        refined_text_dict = dict()
        
        for day in raw_text_dict:
            for article in raw_text_dict[day]:
                refined_text = list()
                soup = BeautifulSoup(test_case)
                html_strip = soup.text

            refined_text_dict[day] = refined_text
                
        return refined_text_dict
    
    def clean_text_file(self, raw_text_file):
        #This function takes an opened file as an input
        #This function removes HTML/XML tags from the raw text files as well as numbers
        
        html_tags = ["\\xa0", "\xa9", "\\u2019s", "\\u201d","\\u201c", '\\u2019', 
                     '\\u2018', '\\u2026', '\\u2014', '\\xfa', 'u2013', '\xc2']
        random_strings = ['pictwittercomjxliJhKCkY', 'BBCBreaking', 'OffenTxfcr', 'nstnUPDATE', 'pictwittercomdhXknZ7KH5',
                         'httpstcoZCwe3oy1mG', 'pictwittercomgkX6IAd8RL', 'httpstcoaPRAjtbv3H', 'dznussbaum']
        refined_text = BeautifulSoup(raw_text_file, "lxml").text
        refined_text = refined_text.replace("SIGN UP FOR OUR NEWSLETTER", " ")
        refined_text = re.sub("[^a-zA-Z]", " ", refined_text)
        text = list(refined_text)
        text = ''.join(text)
        text = text.encode('utf-8')
        
        for tag in html_tags:
            text = text.replace(tag,' ')
            
        for string in random_strings:
            text = text.replace(string,' ')
        return text
    
    def abbrev_clean(self, raw_text):
        #This function takes a string as an input and returns a word list
        #This function performs an Apostrophe Lookup on the words in the list
        combined_text = str().encode('utf-8')
        
        combined_text = raw_text.replace("Can\'t", "Can not")
        combined_text = combined_text.replace("can\'t", "can not")
        combined_text = combined_text.replace("didn\'t", "did not")
        combined_text = combined_text.replace("Didn\'t", "did not")
        combined_text = combined_text.replace("Can \'t", "Can not")
        combined_text = combined_text.replace("can \'t", "can not")
        combined_text = combined_text.replace("didn \'t", "did not")
        combined_text = combined_text.replace("Didn \'t", "did not")
        combined_text = combined_text.replace("it\'s", "it is")
        combined_text = combined_text.replace("It\'s", "It is")
        combined_text = combined_text.replace("it \'s", "it is")
        combined_text = combined_text.replace("It \'s", "It is")
        combined_text = combined_text.replace("we\'ve", "we have")
        combined_text = combined_text.replace("We\'ve", "We have")
        combined_text = combined_text.replace("won\'t", "will not")
        combined_text = combined_text.replace("Won\'t", "Will not")
        combined_text = combined_text.replace("whos", "who is")
        combined_text = combined_text.replace("I\'m", "I am")
        combined_text = combined_text.replace("Im", "I am")
        combined_text = combined_text.replace("WATCH LIVE", " ")
        combined_text = combined_text.replace("Watch live", " ")
        combined_text = re.sub('\\bve\\b','have',combined_text)

        return combined_text
    
    def stop_punc_clean(self, word_list):
        #This function takes a string as an input and returns a word list
        #This function removes stop words and punctuation marks using the nltk module
        word_list = word_list.split(' ')
        StopWords = stopwords.words("english")
        StopWords = [word.encode('utf-8') for word in StopWords]
        word_list = [word for word in word_list if word not in StopWords]
        
        combined_list = ' '.join(word_list)
        combined_list = combined_list.translate(None, '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~')
        word_list_clean = combined_list.split(' ')
        word_list_clean = filter(None, word_list_clean)
        word_list_clean = [word for word in word_list_clean if word != '--']
        return word_list_clean