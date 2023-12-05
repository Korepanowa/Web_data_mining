import pandas as pd
import matplotlib.pyplot as plt
import folium


rmap = folium.Map(
    location=[64.6863136, 97.7453061],
    zoom_start=4
)

museums = pd.read_excel(r"museums.xlsx")
# Выбираем столбец с названиями городов:
cities = museums.iloc[:, 1]   
# Подсчитываем совпадающие наименования городов:                                                          
count = cities.value_counts()                                          
 
print("Города и колличество музеев по градации:")
print(count)

# Получаем координаты для построения карты:
museums['Координаты'] = museums['На карте'].str.rstrip(':').str.split(':').str[2]

coordinates = []
# Собираем координаты в лист:
list_coordinates = []
for column in museums:
    columnSeriesObj = museums['Координаты']
    list_coordinates = columnSeriesObj.values.tolist()


for coordinate in list_coordinates:
    one_coord = []
    # Приводим одну координату к строке:
    str_coordinate = str(coordinate)
    
    separator = str_coordinate.index(',')
    longitude = str_coordinate[1:separator]
    latitude = str_coordinate[separator+1:len(str_coordinate)-2]
    one_coord = [float(latitude), float(longitude)]
    coordinates.append(one_coord)

print(len(coordinates))
for coordinate in range(len(coordinates)):
    folium.Marker(coordinates[coordinate], icon=folium.Icon(color="blue")).add_to(rmap)


rmap.save(r'museum_map.html')


