from bs4 import BeautifulSoup
from collections import Counter
Criterion = open('Criterion.html', encoding="utf8")
soup = BeautifulSoup(Criterion,'html.parser')
directors=['Jean Renoir','Jacques Deray']
u=soup.find(class_="vcard")
y=0
while y != 544:
    k=u.find_next(class_="vcard")
    directors.append(k.text)
    u=k.find_next(class_="vcard")
    directors.append(u.text)
    y+=1
for a in sorted(Counter(directors).items(), key=lambda x: x[1], reverse=True):
    print(a)
input()