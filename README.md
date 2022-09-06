## English Dictionary Application with Qt Designer
> This application is an artificial intelligence integrated desktop application that contains all the topics English words on site <a href="https://www.oxfordlearnersdictionaries.com/topic/" target="_blank">Oxford Dictionary</a>.

**Purpose of the App**: The purpose of this application is,
1. To suggest a word to the user every day along with its detail and sound. 
2. Getting the user to guess 10 words per day.

### CONTENTS
- [Word Scraping][word_scrap]: Scraping all topical words from the web along with types and saving them by category in csv file.
- [Word Detail Scraping][detail_scrap]: Process of scraping words along with their details and saving them in csv file.
- [Word Sound Scraping][sound_scrap]: Process of scraping words along with their sounds and saving them in csv file.
- [All Words Concatenation][word_concat]: Process of combining all word sets and saving them in a single csv file.
- [App Design][interface]: App design with Qt Designer.


### APPLICATION STEPS
- [x] Scraping the words from the site with definitions and sounds in pieces
- [x] Merge and clean all datasets
- [ ] App design with Qt Designer


[word_scrap]: https://github.com/mrkizmaz/English-Dictionary-App/blob/main/word_scraping.py
[detail_scrap]: https://github.com/mrkizmaz/English-Dictionary-App/blob/main/detail_scraping.py
[sound_scrap]: https://github.com/mrkizmaz/English-Dictionary-App/blob/main/sound_scraping.py
[word_concat]: https://github.com/mrkizmaz/English-Dictionary-App/blob/main/allwords_concat.py
[interface]: https://github.com/mrkizmaz/English-Dictionary-App/blob/main/interface.py