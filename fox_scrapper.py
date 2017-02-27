from bs4 import BeautifulSoup
import requests
import re
#Note this probably won't work for the website pre-2010. The way they wrote the code dramatically changed.
class fox_scrapper(object):

    def __init__(self):
        pass
        
    def find_headlines(self, date_range_list):
        
        date_range_dict = dict()
        archive = "https://web.archive.org"
        site = 'http://www.foxnews.com'
        
        for day in date_range_list:
            
            article_list = []
            raw_html = requests.get(archive + day)
            soup = BeautifulSoup(raw_html.text, 'html.parser')
            li_test = soup.find_all("li")
            
            b_tag = [tags.find_all('b') for tags in li_test]
            a_tag = [tags[0].find_all('a') for tags in b_tag if tags]
            article_list = [re.findall(day + ".*/", str(tags[0])) for tags in 
                            a_tag if tags and re.findall(day + ".*/", str(tags[0]))]
            refined_list = list()
            for article in article_list:
                if re.findall(day + ".*/", str(article[0])):
                    if 'slideshow' in re.findall(day + ".*/", str(article[0]))[0].split('">')[0]:
                        continue
                    refined_list.append(re.findall(day + ".*/", str(article[0]))[0].split('">')[0])

            date_range_dict[day] = refined_list
                
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
                content = soup.find_all("div", class_="article-text")
                
                if content:
                    article_dict[article_name] = content[0].find_all("p")
                    
            raw_text_dict[key] = article_dict
       
        return raw_text_dict