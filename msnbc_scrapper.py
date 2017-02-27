from bs4 import BeautifulSoup
import requests
import re
#Note this probably won't work for the website pre-2010. The way they wrote the code dramatically changed.
class msnbc_scrapper(object):

    def __init__(self):
        pass
        
    def find_headlines(self, date_range_list):
        
        date_range_dict = dict()
        archive = "https://web.archive.org"
        site = 'http://www.msnbc.com'
        
        for day in date_range_list:
            
            article_list = []
            raw_html = requests.get(archive + day)
            soup = BeautifulSoup(raw_html.text, 'html.parser')
            #Using MSNBC.com will pull only the videos, while www.nbcnews.com contains all the text articles
            refined_day = day[:20] + 'http://www.nbcnews.com/'
            
            li_test = soup.find_all("li", {'class': re.compile('featured-slider-menu__item featured-slider-menu__item--.*')})
            article_list = [re.findall(refined_day + ".*/", str(tags)) for tags in 
                            li_test if tags and re.findall(refined_day + ".*/", str(tags))]
            refined_list = list()
            
            for article in article_list:
                if re.findall(refined_day + ".*/", str(article[0])):
                    refined_list.append(re.findall(refined_day + ".*/", str(article[0]))[0].split('">')[0])

            date_range_dict[day] = refined_list
                
        return date_range_dict
    
    def headline_scrapper(self, date_range_dict):
        
        archive = "https://web.archive.org"
        raw_text_dict = dict()
        
        for key in date_range_dict.keys():
            article_dict = dict()
            for article in range(0, len(date_range_dict[key])):
                
                article_list = list()
                article_name = date_range_dict[key][article] 
                article_html = requests.get(archive + article_name)
                soup = BeautifulSoup(article_html.text, 'html.parser')
                content = soup.find_all("p")
                refined_content = [p for p in content if not p.find_all('span')]
                
                for line in refined_content:
                    article_list.append(str(line))
                article_dict[article_name] = ' '.join(article_list)
                
            raw_text_dict[key] = article_dict
       
        return raw_text_dict