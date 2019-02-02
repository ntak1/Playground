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
        
        
        

def extract_page_links(node,contain=None, not_contain=None, prefix='https://en.wikipedia.org/'):
    """
    Return a filtered list of links adjacent (present) in a given page. The
    links contain the words specified in contain list, and not contain
    the words specified in not_contain list.
    -node: part of the link that specifies wich Wikipedia's page we want
    to acces.
    -contain: a list of words (strings) that the links returned must contain
    -not_contain: a list of words (strings) that the links returned must
    not contain.
    -prefix: the prefix of the Wikipedia's page, it specifies for example
    the page's language, by default we are serching the in the english
    articles.
    """
    node = prefix + node
    node_response = requests.get(node, timeout=5)
    try:
        assert(node_response.status_code == 200)
    except:
        raise('Request failed')
    node_content = BeautifulSoup(node_response.content, 'html.parser')

    adj_links = [link['href'] for link in node_content.find_all('a', href=True)]
    
    if contain is not None:
        adj_links = [link for link in adj_links for word in contain if
                        word in link]
    if not_contain is not None:
        adj_links = [link for link in adj_links for word in contain if
                    word not in link]
    shuffle(adj_links)
    return adj_links