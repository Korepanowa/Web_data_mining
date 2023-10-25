import wikipedia
import json

result = wikipedia.search("the rarest species of frogs")

# Получим страницу.
page = wikipedia.page(result[0])

# Получим заголовок страницы.
title = page.title

# Получение категорий страницы.
categories = page.categories

# Получим весь текст (содержание) страницы Википедии.
content = page.content

# Получение всех ссылок на странице.
links = page.links

summary = page.summary

data = {
        'title': title,
        'categories': categories,
        'content': content,
        'links': links
}


j = json.dumps(data)
print(j)
