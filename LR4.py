from sklearn.neighbors import NearestNeighbors

import numpy

Films = [
	['Академия вампиров', 5.8, 'ужасы', 'фентази'],
	['Джентельмены', 8.6, 'преступление', 'комедия'],
	['Переводчик', 7.9, 'боевик', 'триллер'],
	['Веном', 6.9, 'фантастика', 'боевик'], 
	['Выжившая', 5.9, 'триллер', 'боевик'],
	['Похищенная', 6.1, 'боевик', 'преступление'],
	['Поезд в пусан', 7.2, 'ужасы', 'боевик'],
	['Дракула', 6.6, 'ужасы', 'драма'],
	['Гнев человеческий', 7.6, 'боевик', 'триллер'],
	['Ловушка времени', 6.7, 'фантастика', 'боевик'],
	['Голодные игры', 7.3, 'фантастика', 'триллер'],
	['Валериан и город тысячи планет', 6.9, 'фантастика', ' боевик'],
	['Плохой и сумасшедший', 8.2, 'боевик', 'комедия'],
	['Другой мир', 7.5, 'фэнтези', 'боевик'],
	['Последний охотник на ведьм', 6.2, 'приключения', 'боевик'],
	['Кунг-фу жеребец', 8.0, 'боевик' ,'драма'],
	['Агент под прикрытием', 5.9, 'боевик', 'комедия'],
	['Патруль', 7.7, 'боевик', 'триллер'],
	['Гангстер, коп и дьявол', 7.3, 'триллер', 'боевик'],
	['Апокалипсис', 8.0, 'боевик', 'триллер'],
	['Робин гуд', 5.9, 'боевик', 'драма'],
	['Джуманджи, зов джунглей', 6.9, 'фэнтези', 'боевик'],
	['Найди меня, если сможешь', 5.9, 'триллер', 'боевик'],
	['Мумия', 7.8, 'приключения', 'боевик'],
	['Время ведьм', 6.2, 'фэнтези', 'боевик'],
	['Игра Эндера', 6.7, 'фантастика', 'боевик'],
	['Вы умрёте, или мы вернём вам деньги', 6.6, 'боевик', 'комедия'],
	['Гладиатор', 9.1, 'история', 'боевик'],
	['Бесславные ублюдки', 8.2, 'боевик', 'драма'],
	['Олдбой', 7.3, 'драма', 'преступление'],
	['Карты, деньги, два ствола', 8.4, 'боевик', 'комедия'],
	['Город грехов', 8.2, 'детектив', 'преступление'],
	['Ультиматум Борна', 8.1, 'боевик', 'детектив'],
	['Миссия Серенити', 7.4, 'фантастика', 'боевик'],
	['Джентельмены', 9.0, 'преступление', 'комедия'],
	['13 Район', 7.8, 'боевик', 'преступление'],
	['Риддик', 7.8, 'фантастика', 'боевик'],
	['Люси', 8.1, 'боевик', 'фантастика'],
	['Коломбиана', 7.8, 'боевик', 'триллер'],
	['Час расплаты', 7.8, 'фантастика', 'боевик'], 
	['Пушки Акимбо', 7.3, 'боевик', 'триллер'],
	['Человек ноября', 7.2, 'боевик', 'триллер'], 
	['Полтора шпиона', 8.3, 'боевик', 'комедия']
]




list_of_viewed = [
	['Волк с Уолл-Стрит', 8.0, 'комедия', 'биография'], 
	['1+1', 8.8, 'драма', 'комедия'], 
	['Достать ножи', 8.1, 'детектив', 'комедия'], 
	['Быстрее пули', 6.7, 'боевик', 'комедия'],
	['Начало', 8.7, 'фантатика', 'боевик'], 
	['Пираты карибского моря: проклятие чёрной жемчужины', 8.4, 'фэнтези', 'боевик'],
	['Брат', 8.2, 'драма', 'преступление'],
	['Леон', 8.7, 'боевик', 'триллер'],
	['Зелёная миля', 9.1, 'драма', 'фэнтези'],
	['Знакомьтесь, Джо Блэк', 8.1, 'драма', 'фэнтези']
]

Recommendations = []

for l in list_of_viewed:
	for f in Films:
		if l[2] == f[2] or l[2] == f[3] or l[3] == f[2] or l[3] == f[3]:
			Recommendations.append([f[0],f[1]])
			last = object()

Recommendations_by_genre = sorted(set(map(tuple, Recommendations)))
name = []
rating = []
for R in Recommendations_by_genre:
	name.append(R[0])
	rating.append([R[1]])



Rating = []
for n in list_of_viewed:
	Rating.append(n[1])

K = NearestNeighbors(n_neighbors=7)
K.fit(rating)

Rating_avg = round((numpy.average(Rating)),1)
_, ratings = K.kneighbors([[Rating_avg]])

Recommendations_by_ratings = [name[i] for i in ratings[0]]

print("Рекомендовано к просмотру:")
for film in Recommendations_by_ratings:
    print(film)







