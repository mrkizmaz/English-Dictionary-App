# Word scraping operations from the website: 'www.oxfordlearnersdictionaries.com'

# required libraries
import re
import requests
import pandas as pd
import time

# request to the site
url = 'https://www.oxfordlearnersdictionaries.com/topic/'
headers = {'User-Agent': 'Mozilla/5.0'}
session_obj = requests.Session()
response = session_obj.get(url, headers = headers).text
time.sleep(2)

# getting title of categories
categories = '<a href="https://www.oxfordlearnersdictionaries.com/topic/category/(.*?)">'
categories_all = re.findall(categories, response, re.MULTILINE | re.DOTALL)

try:
    print('Bütün işlemler yapılandırılıyor, Lütfen bekleyiniz...')

    for category in categories_all:
        cateUrl = 'https://www.oxfordlearnersdictionaries.com/topic/category/' + category
        cateSession = requests.Session()
        cateResponse = cateSession.get(cateUrl, headers = headers).text
        time.sleep(2)

        # sub-categories
        subs = '<a class="topic-box-secondary-heading" href="https://www.oxfordlearnersdictionaries.com/topic/(.*?)">(.*?)<span>'
        sublists = re.findall(subs, cateResponse, re.MULTILINE | re.DOTALL)

        # word scraping
        allWords = []
        wordDataset = pd.DataFrame()
        for sub in sublists:
            subUrl = 'https://www.oxfordlearnersdictionaries.com/topic/' + sub[0]
            subSession = requests.Session()
            subResponse = subSession.get(subUrl, headers = headers).text
            time.sleep(2)
            word = '<a href="/definition/english/(.*?)">(.*?)</a><span class="pos">(.*?)</span><div><span class="belong-to">(.*?)</span>'
            words = re.findall(word, subResponse, re.MULTILINE | re.DOTALL)
            
            # saving the words to dataset
            for i in words:
                allWords.append(i)
                wordDataset = pd.DataFrame(allWords, columns = ['subLink', 'word', 'type', 'level'])
                wordDataset.to_csv(f'Word-Sets/{category}.csv', index_label = False)
                
    time.sleep(2)
    print('Tüm işlemler başarılı bir şekilde tamamlandı.')
except:
    print('Bir hata ile karşılaşıldı. Hatayı tespit edip onarınız lütfen.')

