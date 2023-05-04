import requests
outputs = open('cn_stopwords.txt', 'w', encoding='UTF-8')
stopWords = requests.get("https://raw.githubusercontent.com/goto456/stopwords/master/cn_stopwords.txt")
print(stopWords.text)
outputs.write(stopWords.text)
stopWords.close()