from bs4 import BeautifulSoup
import requests
import re
#Note this probably won't work for the website pre-2010. The way they wrote the code dramatically changed.
class cnn_scrapper(object):

    def __init__(self):
        pass
        
    def find_headlines(self, date_range_list):
        
        date_range_dict = dict()
        archive = "https://web.archive.org"
        subsites = ['http://www.cnn.com', 'http://money.cnn.com', "http://bleacherreport.com"]
        
        for day in date_range_list:
            article_list = list()
            raw_html = requests.get(archive + day)
            soup = BeautifulSoup(raw_html.text, 'html.parser')
            
            articles = soup.find_all("h3", class_="cd__headline")
            
            for article in articles:
                for site in subsites:
                    try:
                        article_url = re.findall(day[:20] + site + ".*/", str(article.find_all(href=True)[0]))[0].split('">')[0]
                        article_list.append(article_url)
 
                    except:
                        continue    
                
            
            date_range_dict[day] = article_list
                
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
                
                if 'video' in date_range_dict[key][article]:
                    continue
                    
                if 'http://www.cnn.com' in article_name:
                    soup = BeautifulSoup(article_html.text, 'html.parser')
                    content = soup.find_all("div", class_="zn-body__paragraph")
                    
                    for line in content:
                        article_list.append(str(line))
                    article_dict[article_name] = ' '.join(article_list)
                
                if 'http://money.cnn.com' in article_name \
                or "http://bleacherreport.com" in article_name:
                    soup = BeautifulSoup(article_html.text, 'html.parser')
                    content = soup.find_all("p")
                    refined_content = [tag for tag in content if not re.findall("class=", str(tag))]
                    
                    for line in refined_content:
                        article_list.append(str(line))
                    article_dict[article_name] = ' '.join(article_list)
                    
            raw_text_dict[key] = article_dict   
            
        return raw_text_dict