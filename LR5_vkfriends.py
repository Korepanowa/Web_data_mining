import requests
import networkx
import time
import collections
import matplotlib.pyplot as plt

# Мои жалике попытки:
# В первую очередь зарегистрировала приложение в вк и получила token и user id, но вот как их правильно использовать так и не поняла, к сожалению.

def get_friends_ids(user_id):
    # Добавила полученный token в запрос friends_url:
    friends_url = 'https://api.vk.com/method/friends.get?user_id={}&access_token=vk1.a.H9c.........................................................................................v=5.131'
    json_response = requests.get(friends_url.format(user_id)).json()
    if json_response.get('error'):
        print(json_response.get('error'))
        return list()
    return json_response[u'response']


graph = {}
# Если честно, так и не разобралась, какой именно user id вставлять, поэтому оставила тот, что был получен с access_token, если вставлять просто id страницы, граф выходит пустой.
friend_ids = get_friends_ids(166342625)  
for friend_id in friend_ids:
    print('Processing id: ', friend_id)
    graph[friend_id] = get_friends_ids(friend_id)

g = networkx.Graph(directed=False)
for i in graph:
    g.add_node(i)
    for j in graph[i]:
        if i != j and i in friend_ids and j in friend_ids:
            g.add_edge(i, j)

# Смотреть скрины.
print(g)
plt.figure(figsize=(10, 10))
pos = networkx.spring_layout(g)
networkx.draw(g, pos, node_size=30, with_labels=False, edge_color='blue', node_color='green')
plt.show()