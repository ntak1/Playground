import requests
from random import shuffle
from bs4 import BeautifulSoup


# A useful function to print an array, en element per line
def print_array(array, limit=None):
    if limit is None:
        limit = len(array)
    for i in range(limit):
        print(array[i])
        i += 1
        
        
        

def extract_page_links(link):
    """
    Extract all the links in a given html page
    Arguments:
        link: the link of the page we want to search for the link
    Return:
        A list with the links
    """
    link_response = requests.get(link, timeout=5)
    try:
        assert(link_response.status_code == 200)
    except:
        print('Request failed')
        
    link_content = BeautifulSoup(link_response.content, 'html.parser')
    adj_links = [link['href'] for link in link_content.find_all('a', href=True)]
        
    shuffle(adj_links)
    return adj_links