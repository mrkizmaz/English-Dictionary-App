# Concatenation all word data sets

# required libraries
import os
import pandas as pd

# examination the total word counts
def totalWords(data):
    df = pd.read_csv(f'Word-Sets/{data}', sep = ',')
    total = df.shape[0]
    return total

total_words_count = 0
for i in os.listdir('Word-Sets'):
    total_word = totalWords(i)
    print(f'{i} veri setinin kelime sayısı: {total_word}')
    total_words_count += total_word
print(f'Toplam kelime sayısı: {total_words_count}') # output --> total word: 29175

# concatenation  
allWordSet = pd.DataFrame()
for i in os.listdir('Word-Sets'):
    data = pd.read_csv(f'Word-Sets/{i}')
    allWordSet = pd.concat([allWordSet, data], ignore_index = True)

# sneak peek to the dataset
print(allWordSet.head(10))
print(allWordSet.info())

# saving the dataset
allWordSet.to_csv('EnglishWords.csv', sep = ',', encoding = 'utf-8', index_label = False)