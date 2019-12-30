#! python3
# lucky.py - Opens several Google search results.

import requests
import bs4
import sys
sys.path.insert(1,'/home/malavan')

print('Googling...') # display text while downloading the Google
res= requests.get('https://google.com/search?q='+"".join(sys.argv[1:]))
