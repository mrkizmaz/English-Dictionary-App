# scraipng the pronunciation of words

# required libraries
import os
import pandas as pd
import time
import re
import requests
import urllib.request
from bs4 import BeautifulSoup

# getting the word sound data with function
def getSoundLinks(dataset):

    df = pd.read_csv(f'Word-Sets/{dataset}')
    link = df['subLink'][0:50].values

    try:
        print(f'{dataset} verisetindeki kelimelerin ses verileri işleniyor, Lütfen bekleyiniz...')
        
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        file_name = dataset.split('.')[0]
        os.mkdir(f'kelimeSesleri/{file_name}Sounds')

        start = time.time()
        sounds = []
        for sub in link:
            
            sublink = 'https://www.oxfordlearnersdictionaries.com/definition/english/' + sub
            response = requests.get(sublink, headers = headers)
            time.sleep(1)

            soup = BeautifulSoup(response.content, 'html.parser')
            result = soup.findAll(attrs={'class': re.compile(r"^sound audio_play_button pron-uk icon-audio$")})

            if len(result) > 0:
                url = result[0]['data-src-mp3']
                file = url.split('/')
                opener = urllib.request.build_opener()
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve(url, f'kelimeSesleri/{file_name}Sounds/{file[-1]}')

                sounds.append(file[-1])

            else:
                sounds.append('No sound!')

        duration = time.time() - start

        df['sound'] = sounds
            
        print(f'{dataset} verisetindeki tüm işlemler başarılı bir şekilde tamamlandı, işlem süresi: {duration} sn.') 
        
    except Exception as e:
        print(f'Bir hata ile karşılaşıldı. Hatayı onarınız; Hatanın nedeni: {e}')

    df.to_csv('leisurewithsounds.csv', index_label = False)
    
    return df.info()

a = getSoundLinks('leisure.csv')
print(a / 60.0)

"""
total_time = 0    
for dataset in os.listdir('Word-Sets'):
    duration = getSoundLinks(dataset)
    time.sleep(1)
    total_time += duration
    print('-------------------------------------------------------------')
    time.sleep(0.5)

print(f'Tüm işlemlerin toplam süresi: {total_time / 60} minutes')
"""