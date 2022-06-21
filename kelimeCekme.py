# Word scraping operations from the website: 'www.oxfordlearnersdictionaries.com'

# required libraries
import re
import requests
import pandas as pd

# request to the 
categories = ['animals_1', 'appearance_1', 'communication']
url = 'https://www.oxfordlearnersdictionaries.com/topic/category/animals_1'
headers = {'User-Agent': 'Mozilla/5.0'}
session_obj = requests.Session()
response = session_obj.get(url, headers = headers).text

# sub-categories
subs = '<a class="topic-box-secondary-heading" href="https://www.oxfordlearnersdictionaries.com/topic/(.*?)">(.*?)<span>'
sublists = re.findall(subs, response, re.MULTILINE | re.DOTALL)

# word scraping
allWords = []
for sub in sublists:
    subUrl = 'https://www.oxfordlearnersdictionaries.com/topic/' + sub[0]
    subSession = requests.Session()
    subResponse = subSession.get(subUrl, headers = headers).text
    word = '<a href="/definition/english/(.*?)">(.*?)</a><span class="pos">(.*?)</span><div><span class="belong-to">(.*?)</span>'
    words = re.findall(word, subResponse, re.MULTILINE | re.DOTALL)
    for i in words:
        allWords.append(i)

wordDataset = pd.DataFrame(allWords, columns = ['subLink', 'word', 'type', 'level'])
wordDataset.to_csv('englishWords.csv', index_label = False)
print(wordDataset.head())
