import requests
from bs4 import BeautifulSoup

from urllib.parse import urljoin


# Указываем URL, с которого будут скачиваться файлы.
url = "https://pstu.ru/title1/faculties/etf/itas/?study=1&cid=80"

# Запрашиваем URL и получаем объект ответа.
response = requests.get(url)

# base_url = response.url

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
	# else:
	# 	href1 = link.get('href')
	# 	url1 = urljoin(base_url, href1)
	# 	response1 = requests.get(url1)
	# 	if response1.status_code == 200:
	# 		soup1 = BeautifulSoup(response1.text, 'html.parser')
	# 		links1 = soup1.find_all('a')

	# 		i1 = 0

	# 		for link1 in links1:
	# 			if ('.pdf' in link1.get('href', [])):
	# 				i1 += 1
	# 				print("Downloading file: ", i1)

	# 				# получим объект ответа для ссылки.
	# 				response1 = requests.get(link1.get('href'))

	# 				# Запись содержимого в pdf.
	# 				pdf1 = open("pdf"+str(i1)+".pdf", 'wb')
	# 				pdf1.write(response.content)
	# 				pdf1.close()
	# 				print("File ", i1, " downloaded")
	# 	else:
	# 		print("ERROR")




print("All PDF files downloaded")
