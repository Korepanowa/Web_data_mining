import wikipedia
import json


# распечатать резюме того, что такое питон
#print(wikipedia.summary("Python Programming Language"))

result = wikipedia.search("the rarest species of frogs")
#print(result)

# получить страницу: Neural network
page = wikipedia.page(result[0])

# получим заголовок страницы
title = page.title

# получение категорий страницы
categories = page.categories

# получить весь текст (содержание) страницы Википедии
content = page.content

# получение всех ссылок на странице
links = page.links


# в итоге
summary = page.summary

data = {
        'title': title,
        'categories': categories,
        'content': content,
        'links': links
}


j = json.dumps(data)
# напечатаем инфо
print(j)