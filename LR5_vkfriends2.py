import vk_api
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import label_propagation_communities

VK_CONFIG = {
    "domain": "https://api.vk.com/method",
    "access_token": "token",  
    "version": "5.124",
}

user_id = 166342625


vk_session = vk_api.VkApi(token=VK_CONFIG['access_token'])
vk = vk_session.get_api()


response = vk.friends.get(user_id=user_id, fields='nickname')
friends = response['items']

G = nx.Graph()

for friend in friends:
    G.add_edge(user_id, friend['id'])

pos = nx.spring_layout(G)

plt.figure(figsize=(10, 10))
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color='yellow', node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='green', arrows=False)
plt.show()

communities = list(label_propagation_communities(G))
print(communities)
