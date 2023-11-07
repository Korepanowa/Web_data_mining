import requests

import graphviz
import networkx 

from bs4 import BeautifulSoup
from itertools import combinations

# Подготовка данных.
urls = [
    {"url": "https://foxford.ru/wiki/geografiya/cvetnaya-metallurgia-rossii?ysclid=loop8urpmq70165277", "keywords": ["цветные металлы", "производство цветных металлов"]},
    {"url": "https://vt-metall.ru/articles/osobennosti-tsvetnoy-metallurgii/?ysclid=loopdbhqh8491191969", "keywords": ["цветные металлы", "цветная металлургия", "классификация", "подотрасли ", "особенности развития"]},
    {"url": "https://obrazovaka.ru/geografiya/cvetnaya-metallurgiya-tablica-9-klass.html?ysclid=loopj1rms0354841767", "keywords": ["цветная металлургия","география цветной металлургии"]},
    {"url": "https://fabricators.ru/article/cvetnaya-metallurgiya?ysclid=looplhld1971421005", "keywords": ["цветные металлы", "классификация", "подотрасли", "цветная металлургия в России"]},
    {"url": "https://bigenc.ru/c/tsvetnaia-metallurgiia-532193?ysclid=loopoh74re254815370", "keywords": ["цветная металлургия"]},
    {"url": "https://ru.wikipedia.org/wiki/%D0%A6%D0%B2%D0%B5%D1%82%D0%BD%D0%B0%D1%8F_%D0%BC%D0%B5%D1%82%D0%B0%D0%BB%D0%BB%D1%83%D1%80%D0%B3%D0%B8%D1%8F", "keywords": ["цветная металлургия", "классификация"]},
    {"url": "https://fb.ru/article/172613/tsvetnaya-metallurgiya-rossii-geografiya-tsvetnoy-metallurgii?ysclid=loopwwq5ee774102655", "keywords": ["цветная металлургия в России", "география цветной металлургии", "подотрасли"]},
    {"url": "https://metallplace.ru/about/stati-o-chernoy-metalurgii/tsvetnaya-metallurgiya/?ysclid=looq11amak709908668", "keywords": ["цветная металлургия в России", "особенности развития"]},
    {"url": "https://мк-союз.рф/metallyi/dobyicha-tsvetnyih-metallov?ysclid=looqab0pg8686583717", "keywords": ["цветная металлургия", "добыча", "отрасли"]},
    {"url": "https://megatrends.su/blog/market-overview-of-non-ferrous-metals/?ysclid=looqlehqp8328579461", "keywords": ["цветные металлы", "классификация"]},
    {"url": "https://metalbulletin.ru/?yclid=10780841235036504063", "keywords": ["отрасли"]},
    {"url": "https://nauchniestati.ru/spravka/geografiya-czvetnoj-metallurgii/", "keywords": ["цветная металлургия", "география цветной металлургии"]},
    {"url": "https://fb.ru/article/172613/tsvetnaya-metallurgiya-rossii-geografiya-tsvetnoy-metallurgii", "keywords": ["цветная металлургия в России", "география цветной металлургии"]},
    {"url": "https://sterbrust.tech/spravochnik/materialovedenie/tsvetnaya-metallurgiya.html?ysclid=looqu15d9t862698746", "keywords": ["цветная металлургия", "отрасли"]},
    {"url": "https://www.metaltorg.ru/", "keywords": ["цветные металлы", "металлоторговля"]},
    {"url": "https://studopedia.su/6_51465_tsvetnaya-metallurgiya.html", "keywords": ["цветная металлургия", "цветная металлургия в России"]},
    {"url": "https://www.booksite.ru/fulltext/1/001/008/120/298.htm", "keywords": ["цветная металлургия в России", "география цветной металлургии"]},
    {"url": "https://metallurgist.pro/metallurgy/non-ferrous/fund-non-ferrous/", "keywords": ["металлургические процессы", "классификация"]},
    {"url": "https://gufo.me/dict/technology_modernenc/%D1%86%D0%B2%D0%B5%D1%82%D0%BD%D0%B0%D1%8F_%D0%BC%D0%B5%D1%82%D0%B0%D0%BB%D0%BB%D1%83%D1%80%D0%B3%D0%B8%D1%8F", "keywords": ["цветная металлургия"]},
    {"url": "https://kartaslov.ru/%D0%BA%D0%B0%D1%80%D1%82%D0%B0-%D0%B7%D0%BD%D0%B0%D0%BD%D0%B8%D0%B9/%D0%A6%D0%B2%D0%B5%D1%82%D0%BD%D0%B0%D1%8F+%D0%BC%D0%B5%D1%82%D0%B0%D0%BB%D0%BB%D1%83%D1%80%D0%B3%D0%B8%D1%8F", "keywords": ["цветная металлургия", "понятия"]},
    {"url": "https://ferrolabs.ru/blog/zvetnye-metally/", "keywords": ["цветные металлы", "классификация"]},
    {"url": "https://geographyofrussia.com/cvetnaya-metallurgiya/?ysclid=loordaxg8b268046074", "keywords": ["цветная металлургия"]},
    {"url": "https://metaprom.ru/articles/a432-cvetnaya-metallurgiya-v-rossii/?ysclid=looreyd324426781742", "keywords": ["цветная металлургия в России"]},
    {"url": "https://studref.com/323407/ekologiya/tsvetnaya_metallurgiya?ysclid=loorgtrtf0668302757", "keywords": ["цветная металлургия", "география цветной металлургии"]},
    {"url": "https://www.metaltorg.ru/", "keywords": ["цветная металлургия", "производство цветных металлов"]}
]

# Перейдём к созданию графа.
graf = networkx.Graph()

for url in urls:
    u = url["url"]
    words = url["keywords"]

    # Получим содержимое страницы.
    response = requests.get(u)                          
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()                                
    
    # Добавим вершину графа.
    graf.add_node(u)    

    # Добавим ключевые термины в качестве атрибутов.
    for key in words:                              
        graf.nodes[u][key] = True

# Определим связи (Между ключевыми словами А и В).
for A, B in combinations(urls, 2):                    
    Awords = set(A["keywords"])
    Bwords = set(B["keywords"])
    connection = Awords.intersection(Bwords)
    
    if connection:
        graf.add_edge(A["url"], B["url"], common_keywords=list(connection))

# Визуализируем полученный граф.
grafD = graphviz.Digraph(comment='Цветная Металлургия')  
grafD.render(r'home/korens/py', view=False)

# Добавим вершины и полученные связи.
for vertex in graf.nodes:       
    grafD.node(vertex)

for edge in graf.edges:
    A, B = edge
    common_keywords = graf.edges[A, B]["common_keywords"]
    record = ", ".join(common_keywords)
    grafD.edge(A, B, label=record)

grafD.render('Граф', view=True) 
