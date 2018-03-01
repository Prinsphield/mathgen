#!/usr/bin/python
'''
Created on 25. 7. 2012.

@author: filip
'''

import urllib
import re
import sys
from graphviz import Digraph

prefix = "http://genealogy.math.ndsu.nodak.edu/id.php?id="
prefix = "http://www.genealogy.ams.org/id.php?id="
cache = {}

dot = Digraph(comment='X''s academic genealogy')

def get_page(url):
    try:
        print url
        return urllib.urlopen(url).read()
    except:
        return ""

def remove_excess_space(s):
    return re.sub(r'\s+', " ", s.strip())

def get_name(page):
    search_result = re.search(r'(.*)</h2>', page) 
    return search_result.group(1) if search_result != None else ""

def get_year(page):
    search_result = re.search(r'(\d{4})</span>', page) 
    return search_result.group(1) if search_result != None else ""

def get_advisor_ids(page):
    return re.findall(r'Advisor.*?:.*?<a href="id\.php\?id=(\d*?)">', page)

def get_advisors_string(advisors):
    if not advisors:
        return ""
    else:
        first = advisors[:-1]
        last = advisors[-1:][0]
        return " (a student of " + ", ".join(first) + (" and " if first else "") + last + ")"
    
def crawl(math_id):
    if math_id not in cache:
        page = get_page(prefix + math_id)
        name = remove_excess_space(get_name(page))
        year = remove_excess_space(get_year(page))
        dot.node(str(math_id), name+"\n"+year)
        cache[math_id] = name+"\n"+year
        #advisors_string = get_advisors_string([crawl(advisor_id) for advisor_id in get_advisor_ids(page)])
        #dot.render()
        import time
        time.sleep(2)

        for advisor_id in get_advisor_ids(page):
            print(advisor_id)

        for advisor_id in get_advisor_ids(page):
            dot.edge(str(advisor_id), str(math_id))
            crawl(advisor_id)

        #return name + advisors_string
    return cache[math_id]
    
if __name__ == '__main__':
    math_id = sys.argv[1] if len(sys.argv) >= 2 else ""
    print crawl(math_id)
