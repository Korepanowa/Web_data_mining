from comcrawl import IndexClient

client = IndexClient()

# Сайты для поиска:
urls = [
    "https://59.ru",
    "https://pstu.ru",
    "https://properm.ru"
]

query = "ИТАС" 
results = client.search(query)

# Создадим список для содержаний и адресов.

list_r = []                                                                 

# Вводим ограничение на количество результатов.
max_r = 10                                                                 
count = 10

for result in results:                                                          
    url = result.url
    if any(domain in url for domain in urls):                            
        text = result.text
        list_r.append((url, text))
        count += 1
        if count >= max_r:                                                                      
            break

data = pd.DataFrame(list_r, columns=['URL-адрес', 'Текст']) 

                                    
print(data)
