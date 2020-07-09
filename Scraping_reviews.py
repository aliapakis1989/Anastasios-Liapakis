from bs4 import BeautifulSoup
import requests
import json
list=[]

url = 'https://www.e-food.gr/delivery/ilion/gyradiko-o-daskalos#pills-ratings'
res = requests.get(url)
soup = BeautifulSoup(res.text, features="lxml")
text = res.text

userIdText = 'app.userSid = '
pos = text.find(userIdText)
start = pos + len(userIdText)
userId = text[start:start + 34]
#print(userId)

restText = 'var restaurant_id = '
pos = text.find(restText)
start = pos + len(restText)
restId = text[start:start + 7]
#print(restId)

limit = soup.find("a", {"id": "ratings-tab"})
print(limit.text)
start = limit.text.find('(') + 1
end = limit.text.find(')')
limit = limit.text[start:end]
#print(limit)

headers = {"X-core-session-id": userId,
           "Accept-Language": 'el',
           "X-core-platform": 'web',
           "X-core-version": '3'
           }
url = 'https://api.e-food.gr/api/v1/restaurants/' + restId + '/ratings/?limit=' + limit
response = requests.get(url, headers=headers)  # modify request headers
#print(response.headers)  # print response headers
#print(response.headers['Content-Type'])
#print(response.text)
resp = json.loads(response.text)
#print(resp['data'])
for comm in resp['data']:
    if comm['comment']:
        list.append(comm['comment'])
print(list)
print(len(list))
