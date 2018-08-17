import requests
from bs4 import BeautifulSoup
# import re
import nltk
nltk.download('punkt')
page = requests.get('https://en.wikipedia.org/wiki/Cars_(film)')

soup = BeautifulSoup(page.content, 'html.parser')
text = soup.get_text()
# print(text)
# ps = 'p\w+'
# re.findall(ps, text)
sent_text = nltk.sent_tokenize(text)
# print(sent_text)
x = input("enter the keyword")
for i,j in enumerate(sent_text):
    if x in sent_text[i]:
        print(sent_text[i])
    else:
        continue
        #print('string not found')