import os
import pandas as pd
import time
import re
import requests
import urllib.request
from bs4 import BeautifulSoup

df = pd.read_csv('Word-Sets/health.csv')
link = df['subLink'].values[0:50]

try:
    print('İşlemler yapılandırılıyor, Lütfen bekleyiniz...')

    headers = {'User-Agent': 'Mozilla/5.0'}

    definitions = []
    for sub in link:
        print(f'{len(definitions)} adet tanım verisi çekildi. İşlemler devem ediyor...')

        sublink = 'https://www.oxfordlearnersdictionaries.com/definition/english/' + sub
        response = requests.get(sublink, headers = headers)
        time.sleep(0.5)

        soup = BeautifulSoup(response.content, 'html.parser')
        result = soup.findAll(attrs={'class': re.compile(r"^def$")})

        if len(result) > 0:
            nesne = [str(result[0])]
            result2 = list(map(lambda text: re.sub(re.compile('<.*?>'), '', text), nesne))
            definitions.append(result2[0].strip('"'))
        else:
            definitions.append('No definition!')

    print('Bütün işlemler başarılı bir şekilde tamamlandı.')

    new_df = pd.DataFrame({'word': df['word'].values[0:50], 'definition': definitions})
    new_df.to_csv('Definition-Sets/healthDefinitions.csv', index_label = False)

except Exception as e:
    print(f'Bir hata ile karşılaşıldı. Hatayı onarınız; Hatanın nedeni: {e}')
