from bs4 import BeautifulSoup
import requests

url = "https://play.google.com/store/games"
res = requests.get(url)
# print(res.text)
# exit()
soup = BeautifulSoup(res.text, 'html.parser')
card_list = soup.select('div.card-list')
print(card_list)
exit()

print(">>>>>>", card_list.get('class'))
for i in card_list:
    cards = i.select('.card')
    for c in cards:
        print(">>, c.get('class)")

