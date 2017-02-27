from bs4 import BeautifulSoup
import requests
import re

class breitbart_scrapper(object):

    def __init__(self):
        pass
        
    def find_headlines(self, date_range_list):
        
        date_range_dict = dict()
        archive = "https://web.archive.org"
        
        for day in date_range_list:
            article_list = list()
            raw_html = requests.get(archive + day)
            soup = BeautifulSoup(raw_html.text, 'html.parser')
            
            articles = soup.find_all("div", class_="article-content")
            
            for article in articles:
                try:
                    article_url = re.findall(day + ".*/", str(article.find_all(href = True)))[0].split('">')[0]
                    article_list.append(article_url)
                except:
                    print "Something went wrong with parsing the front page"
            
            date_range_dict[day] = article_list
                
        return date_range_dict
    
    def headline_scrapper(self, date_range_dict):
        
        archive = "https://web.archive.org"
        raw_text_dict = dict()
        
        for key in date_range_dict.keys():
            article_dict = dict()
            for article in range(0, len(date_range_dict[key])):
                
                if 'video' in date_range_dict[key][article]:
                    continue
                
                article_name = date_range_dict[key][article] 
                article_html = requests.get(archive + article_name)
                soup = BeautifulSoup(article_html.text, 'html.parser')
                content = soup.find_all("div", class_="entry-content")
                
                if content:
                    article_dict[article_name] = content[0].find_all("p")
                    
            raw_text_dict[key] = article_dict
       
        return raw_text_dict