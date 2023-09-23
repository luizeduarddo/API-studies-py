#%%
import requests
from bs4 import BeautifulSoup as bs
#%%
url = 'https://portalcafebrasil.com.br/todos/podcasts/'
#%%
ret = requests.get(url)
ret.text
#%%
soup = bs(ret.text)
soup
#%%
soup.find('h5').text #Find the first tag h5 in the code
#%%
soup.find('h5').a['href'] #Find tag h5 and tag href to get a link
#%%
lst_podcast = soup.find_all('h5') #Find all the tags h5 in the first webpage
#%%
# For will select each item in list and print the title and link for podcast
for item in lst_podcast:
    print(f"EP: {item.text} - Link: {item.a['href']}")