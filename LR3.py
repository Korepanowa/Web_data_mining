import requests

import random

import matplotlib.pyplot as plt
import numpy as np


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
url6 = "https://bloknot-stavropol.ru/search/?q=%D0%B5%D0%B4%D0%B0&s=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA"
url7 = "https://saratov24.tv/search/?q=%D0%B5%D0%B4%D0%B0"

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

# Самое популярное блюдо в Ставрополе.
w1_ur6 = count_word(url6, word1)
w2_ur6 = count_word(url6, word2)
w3_ur6 = count_word(url6, word3)
w4_ur6 = count_word(url6, word4)
w5_ur6 = count_word(url6, word5)
w6_ur6 = count_word(url6, word6)
w7_ur6 = count_word(url6, word7)
w8_ur6 = count_word(url6, word8)
w9_ur6 = count_word(url6, word9)
w10_ur6 = count_word(url6, word10)

dines6 = {
'хинкали': w1_ur6, 'пицца': w2_ur6, 'роллы': w3_ur6, 'шашлык': w4_ur6, 'шаурма': w5_ur6, 
'картошка фри': w6_ur6,  'бургер': w7_ur6,'хот-дог': w8_ur6, 'самса': w9_ur6, 'блины': w10_ur6
}

max6 = max(dines6, key=dines6.get)
print("Наиболее популярное блюдо в городе Ставрополь:", max6)

# Самое популярное блюдо в Саратове.
w1_ur7 = count_word(url7, word1)
w2_ur7 = count_word(url7, word2)
w3_ur7 = count_word(url7, word3)
w4_ur7 = count_word(url7, word4)
w5_ur7 = count_word(url7, word5)
w6_ur7 = count_word(url7, word6)
w7_ur7 = count_word(url7, word7)
w8_ur7 = count_word(url7, word8)
w9_ur7 = count_word(url7, word9)
w10_ur7 = count_word(url7, word10)

dines7 = {
'хинкали': w1_ur7, 'пицца': w2_ur7, 'роллы': w3_ur7, 'шашлык': w4_ur7, 'шаурма': w5_ur7, 
'картошка фри': w6_ur7,  'бургер': w7_ur7,'хот-дог': w8_ur7, 'самса': w9_ur7, 'блины': w10_ur7
}

max7 = max(dines7, key=dines7.get)
print("Наиболее популярное блюдо в городе Саратов:", max7)

def data_distribution(array, cluster): 
    cluster_content = [[] for i in range(k)]
    n = len(array)  
    dim = len(array[0])
    for i in range(n):
        min_distance = float('inf')
        situable_cluster = -1
        for j in range(k):
            distance = 0
            for q in range(dim):
                distance += (array[i][q]-cluster[j][q])**2
                        
            distance = distance**(1/2)
            if distance < min_distance:
                min_distance = distance
                situable_cluster = j

        cluster_content[situable_cluster].append(array[i])
        
    return cluster_content


def cluster_update(cluster, cluster_content, dim):
    n = len(array)  
    dim = len(array[0])
    k = len(cluster)
    for i in range(k): #по i кластерам
        for q in range(dim): #по q параметрам
            updated_parameter = 0
            for j in range(len(cluster_content[i])): 
                updated_parameter += cluster_content[i][j][q]
            if len(cluster_content[i]) != 0:
                updated_parameter = updated_parameter / len(cluster_content[i])
            cluster[i][q] = updated_parameter
    return cluster

def clusterization(array, k):
    n = len(array)  
    dim = len(array[0])  

    cluster = [[0 for i in range(dim)] for q in range(k)] 
    cluster_content = [[] for i in range(k)] 

    for i in range(dim):
        for q in range(k):
            cluster[q][i] = random.randint(0, 10) 

    cluster_content = data_distribution(array, cluster)
    
    print(cluster_content)

    

k = 10
dines = ["хинкали", "пицца", "роллы", "шашлык", "шаурма", "картошка фри", "бургер", "хот-дог", "самса", "блины"]
array = [ [dines.index(max1)], [dines.index(max2)], [dines.index(max3)], [dines.index(max4)], [dines.index(max5)], [dines.index(max6)], [dines.index(max7)]]
print(array)
cluster = clusterization(array, k)




