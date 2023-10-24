import os
import requests

from tqdm import tqdm
from bs4 import BeautifulSoup as bs

from urllib.parse import urljoin, urlparse


# Создадим валидатор, который проверит, является ли переданный URL-адрес действительным.
def valid(url):
    # Разбираем URL-адрес на составные части и ищем в них имя домена(netloc) и протокол(scheme).
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


# Определим все URL-адреса изображений на веб-странице.
def get_all_images(url):
    # Возвращаем все URL-адреса изображений по одному 'url'.
    soup = bs(requests.get(url).content, "html.parser")
    urls = []
    # HTML-содержимое веб-страницы находится в объекте "soup", чтобы извлечь все теги "img" в HTML, 
    # используем метод "soup.find_all("img")".
    for img in tqdm(soup.find_all("img"), "Получено изображение"):
        img_url = img.attrs.get("src")
        if not img_url:
            # Пропуск, если "img" не содержит атрибута "src".
            continue
        # Получили все элементы "img" в виде списка.
        # Сделаем URL абсолютным, присоединив имя домена к только что извлеченному URL.
        img_url = urljoin(url, img_url)
        # удалим URL‑адреса, содержащие пары ключ-значение метода GET HTTP-протокола.
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        # Получаем позицию символа "?", а затем после него всё удаляем, в случае его отсутствия возникает исключение.
        # Убедимся, что URL действителен и возвращает все URL-адреса изображений.
        if valid(img_url):
            urls.append(img_url)
    return urls


# Загрузим файл по URL‑адресу и помещает его в созданную папку.
def download(url, pathname):
    # Если путь не существует, сделаем этот путь "dir"
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # Загружаем тело ответа по частям.
    response = requests.get(url, stream=True)

    # Получим общий размер файла.
    file_size = int(response.headers.get("Content-Length", 0))

    # Получим имя файла.
    filename = os.path.join(pathname, url.split("/")[-1])

    # Индикатор выполнения, изменение единицы измерения на байты вместо итераций (по умолчанию tqdm).
    progress = tqdm(response.iter_content(1024), f"Загружен {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            # записываем прочитанные данные в файл.
            f.write(data)
            # Обновляем индикатор выполнения.
            progress.update(len(data))

def main(url, path):
    # Получаем все изображения.
    imgs = get_all_images(url)
    for img in imgs:
        download(img, path)

    

main("https://unsplash.com/s/photos/chine", "/home/korens/py/imag")

