# scraping the pronunciation of words

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
    link = df['subLink'].values

    try:
        print(f'{dataset} verisetindeki kelimelerin ses verileri işleniyor, Lütfen bekleyiniz...')
        
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        file_name = dataset.split('.')[0]
        os.mkdir(f'kelimeSesleri/Sounds_{file_name}')

        start = time.time()
        sounds = []
        for sub in link:
            print(f'{len(sounds)} adet ses verisi çekildi.. İşlemler devem ediyor...')

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
                urllib.request.urlretrieve(url, f'kelimeSesleri/Sounds_{file_name}/{file[-1]}')

                sounds.append(file[-1])

            else:
                sounds.append('No sound!')

        duration = time.time() - start

        df['sound'] = sounds
            
        print(f'{dataset} verisetindeki tüm işlemler başarılı bir şekilde tamamlandı, işlem süresi: {duration} sn.') 
        
    except Exception as e:
        print(f'Bir hata ile karşılaşıldı. Hatayı onarınız; Hatanın nedeni: {e}')

    df_new = df[['word', 'sound']]
    df_new.to_csv(f'Sound-Sets/Sound_{dataset}', index_label = False)
    
    return duration

a = getSoundLinks('leisure.csv')
print(f'Toplam geçen süre: {(a / 60).__trunc__()} dk. {a % 60} sn.')


"""
# with manually
# leisure.csv                ---> processing time: 25 dk 2.4 sn 
# animals_1.csv              ---> processing time: -
# people.csv                 ---> processing time: -
# functions.csv              ---> processing time: -
# communication.csv          ---> processing time: -
# culture.csv                ---> processing time: -
# notions.csv                ---> processing time: -
# sport.csv                  ---> processing time: -
# health.csv                 ---> processing time: -
# appearance_1.csv           ---> processing time: -
# the-natural-world.csv      ---> processing time: -
# homes-and-buildings.csv    ---> processing time: -
# food-and-drink.csv         ---> processing time: -
# science-and-technology.csv ---> processing time: -
# travel.csv                 ---> processing time: -
# work-and-business.csv      ---> processing time: -
# politics-and-society.csv   ---> processing time: -
# time-and-space.csv         ---> processing time: -

"""


"""
# sequential processing of data sets otomatically
total_time = 0    
for dataset in os.listdir('Word-Sets'):
    duration = getSoundLinks(dataset)
    time.sleep(1)
    total_time += duration
    print('-------------------------------------------------------------')
    time.sleep(5)

print(f'Tüm işlemlerin toplam süresi: {total_time / 60} minutes')
"""