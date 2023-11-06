import requests

def count_word(url, word):
    response = requests.get(url)
    # Проверяем на успешный ответ.
    if response.status_code == 200:
        content = response.text.lower()
        count = content.count(word)
        return count
    else:
        return "Не удалось получить доступ к веб-странице"


url1 = "https://properm.ru/search?q=%D0%B5%D0%B4%D0%B0"
url2 = "https://msk1.ru/text/?rubric=food"
url3 = "https://74.ru/text/?rubric=food"
url4 = "https://kazanfirst.ru/search?search-field=%D0%B5%D0%B4%D0%B0"
url5 = "https://www.e1.ru/text/?rubric=food"

word1 = "хинкали"
word2 = "пицца"
word3 = "роллы"
word4 = "шашлык"
word5 = "шаурма"
word6 = "картошка фри"
word7 = "бургер"
word8 = "хот-дог"
word9 = "самса"
word10 = "блины"

# Самое популярное блюдо в Перми.
w1_ur1 = count_word(url1, word1)
w2_ur1 = count_word(url1, word2)
w3_ur1 = count_word(url1, word3)
w4_ur1 = count_word(url1, word4)
w5_ur1 = count_word(url1, word5)
w6_ur1 = count_word(url1, word6)
w7_ur1 = count_word(url1, word7)
w8_ur1 = count_word(url1, word8)
w9_ur1 = count_word(url1, word9)
w10_ur1 = count_word(url1, word10)

dines1 = {
'хинкали': w1_ur1, 'пицца': w2_ur1, 'роллы': w3_ur1, 'шашлык': w4_ur1, 'шаурма': w5_ur1, 
'картошка фри': w6_ur1,  'бургер': w7_ur1,'хот-дог': w8_ur1, 'самса': w9_ur1, 'блины': w10_ur1
}

max1 = max(dines1, key=dines1.get)
print("Наиболее популярное блюдо в городе Пермь:", max1)

# Самое популярное блюдо в Москве.
w1_ur2 = count_word(url2, word1)
w2_ur2 = count_word(url2, word2)
w3_ur2 = count_word(url2, word3)
w4_ur2 = count_word(url2, word4)
w5_ur2 = count_word(url2, word5)
w6_ur2 = count_word(url2, word6)
w7_ur2 = count_word(url2, word7)
w8_ur2 = count_word(url2, word8)
w9_ur2 = count_word(url2, word9)
w10_ur2 = count_word(url2, word10)

dines2 = {
'хинкали': w1_ur2, 'пицца': w2_ur2, 'роллы': w3_ur2, 'шашлык': w4_ur2, 'шаурма': w5_ur2, 
'картошка фри': w6_ur2,  'бургер': w7_ur2,'хот-дог': w8_ur2, 'самса': w9_ur2, 'блины': w10_ur2
}

max2 = max(dines2, key=dines2.get)
print("Наиболее популярное блюдо в городе Москва:", max2)

# Самое популярное блюдо в Челябинске.
w1_ur3 = count_word(url3, word1)
w2_ur3 = count_word(url3, word2)
w3_ur3 = count_word(url3, word3)
w4_ur3 = count_word(url3, word4)
w5_ur3 = count_word(url3, word5)
w6_ur3 = count_word(url3, word6)
w7_ur3 = count_word(url3, word7)
w8_ur3 = count_word(url3, word8)
w9_ur3 = count_word(url3, word9)
w10_ur3 = count_word(url3, word10)

dines3 = {
'хинкали': w1_ur3, 'пицца': w2_ur3, 'роллы': w3_ur3, 'шашлык': w4_ur3, 'шаурма': w5_ur3, 
'картошка фри': w6_ur3,  'бургер': w7_ur3,'хот-дог': w8_ur3, 'самса': w9_ur3, 'блины': w10_ur3
}

max3 = max(dines3, key=dines3.get)
print("Наиболее популярное блюдо в городе Челябинск:", max3)

# Самое популярное блюдо в Казани.
w1_ur4 = count_word(url4, word1)
w2_ur4 = count_word(url4, word2)
w3_ur4 = count_word(url4, word3)
w4_ur4 = count_word(url4, word4)
w5_ur4 = count_word(url4, word5)
w6_ur4 = count_word(url4, word6)
w7_ur4 = count_word(url4, word7)
w8_ur4 = count_word(url4, word8)
w9_ur4 = count_word(url4, word9)
w10_ur4 = count_word(url4, word10)

dines4 = {
'хинкали': w1_ur4, 'пицца': w2_ur4, 'роллы': w3_ur4, 'шашлык': w4_ur4, 'шаурма': w5_ur4, 
'картошка фри': w6_ur4,  'бургер': w7_ur4,'хот-дог': w8_ur4, 'самса': w9_ur4, 'блины': w10_ur4
}

max4 = max(dines4, key=dines4.get)
print("Наиболее популярное блюдо в городе Казань:", max4)

# Самое популярное блюдо в Екатеринбурге.
w1_ur5 = count_word(url5, word1)
w2_ur5 = count_word(url5, word2)
w3_ur5 = count_word(url5, word3)
w4_ur5 = count_word(url5, word4)
w5_ur5 = count_word(url5, word5)
w6_ur5 = count_word(url5, word6)
w7_ur5 = count_word(url5, word7)
w8_ur5 = count_word(url5, word8)
w9_ur5 = count_word(url5, word9)
w10_ur5 = count_word(url5, word10)

dines5 = {
'хинкали': w1_ur5, 'пицца': w2_ur5, 'роллы': w3_ur5, 'шашлык': w4_ur5, 'шаурма': w5_ur5, 
'картошка фри': w6_ur5,  'бургер': w7_ur5,'хот-дог': w8_ur5, 'самса': w9_ur5, 'блины': w10_ur5
}

max5 = max(dines5, key=dines5.get)
print("Наиболее популярное блюдо в городе Екатеринбург:", max5)


