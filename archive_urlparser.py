import requests
import re

class archive_parser(object):

    def __init__(self):
        pass
        
    def find_links(self, url, date_list):
        
        date_range_links = list()
        archive = "https://web.archive.org"
        
        for day in date_list:
            raw_html = requests.get(archive + "/web/" + day + "000000" + "*/" + url)
            links = re.findall("/web/"+ day + ".*/" + url, raw_html.text)
            try:
                date_range_links.append(links[int(len(links)/2)])
            except IndexError:
                print day
            
        return date_range_links