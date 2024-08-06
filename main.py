# import numpy as np 

# # Массив размером (5)
# array_1 = np.zeros(5)

# # Массив размером (5, 4)
# array_2 = np.zeros((5, 4))

# # Массив размером (5, 10, 2)
# array_3 = np.zeros((5, 10, 2))

# print("array_1:", array_1)
# print("array_2:", array_2)
# print("array_3:", array_3)

# import numpy as np

# # Создаем массив с числами от 0 до 10
# array_1 = np.arange(11)

# # Создаем массив с числами от 5 до 15
# array_2 = np.arange(5, 16)

# # Вычисляем скалярное произведение
# dot_product = np.dot(array_1, array_2)

# print("array_1:", array_1)
# print("array_2:", array_2)
# print("Скалярное произведение:", dot_product)

# import numpy as np

# # Создаем массив с числами от 15 до 105 с шагом 2
# array = np.arange(15, 106, 2)

# # Вычисляем среднее значение
# mean_value = np.mean(array)

# print("array:", array)
# print("Среднее значение:", mean_value)

# import numpy as np
#
# # Шаг 1: Создаем массив
# array = np.array([2, 5, 3, 6, 8, 11, 13])
#
# # Шаг 2: Умножаем все элементы на 5
# array = array * 5
#
# # Шаг 3: Возводим все элементы в степень 0.25
# array = array ** 0.25
#
# # Шаг 4: Считаем медианное значение
# median_value = np.median(array)
#
# print("Результирующий массив:", array)
# print("Медианное значение:", median_value)

# import pandas as pd
# from io import StringIO
#
#
# csv_data = '''name,habitat,color,weight,shop_price,iq_score
# lion,land,brown,200.0,500,40
# dolphin,water,gray,150.0,1000,30
# eagle,air,black,5.0,250,50
# bear,land,brown,300.0,1000,25
# turtle,water,green,10.0,150,15
# tiger,land,orange,250.0,800,35
# shark,water,gray,1000.0,2000,10
# hawk,air,brown,2.0,100,55
# elephant,land,gray,4000.0,15000,15
# crocodile,water,green,500.0,600,20
# penguin,land/water,black and white,20.0,200,25
# parrot,air,multi-colored,1.0,500,45
# giraffe,land,yellow,1500.0,10000,30
# jellyfish,water,transparent,0.5,50,5
# otter,water,brown,30.0,300,40
# chameleon,land,green,0.1,100,60
# polar bear,land/ice,white,800.0,2000,20
# koala,land,gray,10.0,500,35
# dove,air,white,0.5,20,25
# rhinoceros,land,gray,2000.0,12000,15
# whale,water,gray,50000.0,500000,10
# snake,land,green,2.0,50,30
# octopus,water,multi-colored,5.0,300,40
# cat,land,orange,5.0,100,35
# swan,water,white,10.0,150,30
# gorilla,land,black,300.0,8000,25
# cockatoo,air,white,1.0,500,50
# hippopotamus,water,gray,4000.0,15000,10
# spider,land,black,0.005,10,60
# pelican,land/water,white,7.0,200,35
# fox,land,red,10.0,300,40
# crab,water,red,0.2,20,25
# rabbit,land,gray,2.0,50,55
# bat,air,black,0.1,30,45
# wolf,land,gray,30.0,800,40
# platypus,water,gray,1.0,500,45
# zebra,land,black and white,500.0,3000,30
# lizard,land,green,0.5,50,50
# seagull,air,white,0.5,30,40
# orangutan,land,orange,50.0,5000,25
# panda,land,black and white,200.0,10000,20
# camel,land,brown,1000.0,7000,15
# raccoon,land,gray,10.0,200,35
# hedgehog,land,brown,0.5,50,55
# monkey,land,brown,20.0,2000,30
# toucan,air,black and yellow,0.5,150,45
# gazelle,land,brown,150.0,1000,35
# cheetah,land,yellow and black,120.0,1500,40
# hammerhead shark,water,gray,500.0,2000,30
# owl,land/air,brown and white,1.0,200,50
# tarantula,land,brown,0.1,50,60
# flamingo,land/water,pink,3.0,150,35
# jaguar,land,orange and black,100.0,1800,35
# '''
#
# animals = pd.read_csv(StringIO(csv_data), index_col='name')
# print(animals.head())
#
# crocodile_price = animals.loc['crocodile', 'shop_price']
# print(f"Цена крокодила: {crocodile_price} долларов")
#
# land_animals = animals[animals['habitat'] == 'land']
# average_price_land = land_animals['shop_price'].mean()
# print(f"Средняя цена животных, обитающих на земле: {average_price_land:.2f} долларов")
#
# max_iq = animals['iq_score'].max()
# smartest_animals = animals[animals['iq_score'] == max_iq].index.tolist()
# print(f"Животные с наибольшим IQ: {smartest_animals}")
#
# height_data = '''name,height
# lion,1.2
# dolphin,2.0
# eagle,0.35
# bear,1.5
# turtle,0.3
# tiger,1.1
# shark,6.0
# hawk,0.5
# elephant,3.5
# crocodile,2.5'''
#
# # Чтение данных в DataFrame
# height = pd.read_csv(StringIO(height_data))
#
# # Соединение данных по именам животных
# df = animals.merge(height, on='name', how='left')
# print("DataFrame после объединения с данными о росте:")
# print(df.head())
#
# import matplotlib.pyplot as plt
#
# flying_animals = df[df['habitat'] == 'air']
#
# plt.figure(figsize=(10, 6))
# plt.hist(flying_animals['height'].dropna(), bins=10, alpha=0.75)
# plt.title('Гистограмма роста всех летающих животных')
# plt.xlabel('Рост (м)')
# plt.ylabel('Количество')
# plt.show()
