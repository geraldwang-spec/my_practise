import requests

url = 'https://jsonplaceholder.typicode.com/posts'
data=requests.get(url).json()
print('total=', len(data))
print(data[0])

for post in data:
    if post['userId'] == 2:
        print(post['title']+'\n')

