import requests
from bs4 import BeautifulSoup


# Указываем URL, с которого будут скачиваться файлы.
url = "https://pstu.ru/title1/faculties/etf/itas/?study=1&cid=80"

# Запрашиваем URL и получаем объект ответа.
response = requests.get(url)

# Анализируем полученный текст.
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все гиперссылки, присутствующие на веб-странице
links = soup.find_all('a')

i = 0

# Проверка ссылок в формате pdf.
# Загружаем файлы при их наличии.
for link in links:
	if ('.pdf' in link.get('href', [])):
		i += 1
		print("Downloading file: ", i)

		# получим объект ответа для ссылки.
		response = requests.get(link.get('href'))

		# Запись содержимого в pdf.
		pdf = open("pdf"+str(i)+".pdf", 'wb')
		pdf.write(response.content)
		pdf.close()
		print("File ", i, " downloaded")

print("All PDF files downloaded")
