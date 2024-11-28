# УСТАНОВКА ПРОИЗВОДИТСЯ ЧЕРЕЗ КОМАНДУ pip install requests
# Библиотека requests является стандартным инструментом для составления HTTP-запросов в Python. Простой и аккуратный API
# значительно облегчает трудоемкий процесс создания запросов.
# Таким образом, можно сосредоточиться на взаимодействии со службами и использовании данных в приложении.
import requests
print('---------------------------------------------------------------------------------------')
print('----------------------↓↓↓↓↓--РАБОТА С БИБЛИОТЕКОЙ REQUESTS--↓↓↓↓↓----------------------')
print('---------------------------------------------------------------------------------------')
response = requests.get('https://api.github.com')
response.encoding = 'utf-8'  # Optional: requests infers this internally
print(response.status_code)
print(response.content)
print(response.text)
print(response.headers)

# УСТАНОВКА ПРОИЗВОДИТСЯ ЧЕРЕЗ КОМАНДУ pip install pandas
# Библиотека pandas позволяет быстро выполнить или автоматизировать работу по фильтрации и сортировке данных, их
# изменению, удалению или заполнению пропусков.
# Помогает подготовить и провести первичный анализ данных для дальнейшего использования в машинном или глубоком обучении.
# Поддерживает основные статистические методы, которые необходимы для работы с данными, например: расчет
# средних значений, их распределение по квантилям и другие.
import pandas as pd
print('-----------------------------------------------------------------------------------------')
print('------------------------↓↓↓↓↓--РАБОТА С БИБЛИОТЕКОЙ PANDAS--↓↓↓↓↓------------------------')
print('-----------------------------------------------------------------------------------------')
list = pd.read_csv('Яблоки.csv', encoding='UTF-8')
show1 = list.head(4)
balance = pd.read_csv('Яблоки.csv', encoding='UTF-8', usecols=[1], header=None)
balance.columns = ['']
balance.drop(0, inplace=True)
balance = balance.apply(pd.to_numeric)
print(show1, '\n...')
balance_average = round(balance.mean(), 1)
result = ['Все сыты! Замечательно!' if x > 1 else 'Кто-то мало поел?' for x in balance_average]
print('В среднем каждый съел ', balance_average, [result])

# Библиотека numpy позволяет производить анализ данных, машинное обучение и научные вычисления, а также существенно
# облегчает обработку векторов и матриц; позволяет осуществлять обработку аудиофайлов и изображений через
# корректировку данных "матрицы" конкретного объекта; и очень много чего ещё...
import numpy as np
print('----------------------------------------------------------------------------------------')
print('------------------------↓↓↓↓↓--РАБОТА С БИБЛИОТЕКОЙ NUMPY--↓↓↓↓↓------------------------')
print('----------------------------------------------------------------------------------------')
from PIL import Image # это не по теме нумпай, а для сохранения изображения ***
width = 1000
height = 1000
NotPixel = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
width2 = 100
height2 = 100
QrCode = np.random.randint(0, 255, (height2, width2, 2), dtype=np.uint8)
print(NotPixel)
img = Image.fromarray(NotPixel) # ***
img.save('NotPixel.png') # ***
print(QrCode)
img = Image.fromarray(QrCode) # ***
img.save('QrCode.png') # ***

# Библиотека Matplotlib позволяет визуализировать данные любой сложности, строить разные варианты графиков:
# линейные, трёхмерные, диаграммы рассеяния и другие, а также комбинировать их. Дополнительные библиотеки позволяют
# расширить возможности анализа данных. Например, модуль Cartopy позволяет работать с картографической информацией.
import matplotlib.pyplot as plt
print('---------------------------------------------------------------------------------------')
print('--------------------↖↖↑↑↗↗--РАБОТА С БИБЛИОТЕКОЙ MATPLOTLIB--↖↖↑↑↗↗--------------------')
print('---------------------------------------------------------------------------------------')
x = ['2030', '2040', '2050', '2060', '2070']
y = [8, 2, 3, 9, 5]
z = [4, 7, 1, 6, 10]

plt.bar(x, y, label='Величина прибыли', alpha=0.5) # столбчатая диаграмма
plt.plot(x, y, color='red', marker='x') # линейный график
plt.xlabel('Год')
plt.ylabel('Прибыль, в млн руб.')
plt.title('Пример столбчатой диаграммы и линейного графика')
plt.legend()
plt.show()

plt.scatter(x, y) # рассеянный график
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('Рассеянный график')
plt.show()

plt.pie(y, labels=x, autopct='%1.1f%%') # круговая диаграмма
plt.title('Круговая диаграмма')
plt.show()

width = 0.35
fig, ax = plt.subplots() # столбчатый график с накоплением
ax.bar(x, y, width, label='y-значения')
ax.bar(x, z, width, bottom=y, label='z-значения')
ax.set_ylabel('Соотношение, в %')
ax.set_title('Столбчатый график с накоплением')
ax.legend(loc='lower left', title='Легенда')
plt.show()
print('--------------------------------ПОКАЗ ГРАФИКОВ ЗАКОНЧЕН--------------------------------')

# УСТАНОВКА ПРОИЗВОДИТСЯ ЧЕРЕЗ КОМАНДУ pip3 install pillow
# Библиотека pillow позволяет обрабатывать графику в Python, получать подробную информацию об изображении,
# создавать новые изображения печатать фото и многое другое.
from PIL import Image, ImageDraw, ImageFont
print('------------------------------------------------------------------------------------------')
print('------------------------↓↓↓↓↓--РАБОТА С БИБЛИОТЕКОЙ PILLOW--↓↓↓↓↓-------------------------')
print('------------------------------------------------------------------------------------------')
image = Image.open('image_kitten.jpg')
image.crop((793, 357, 4513, 2745)).save('cropped_image.png')
image2 = Image.open('cropped_image.png')
gray_image = image2.convert('L')
write_text = ImageDraw.Draw(gray_image)
text = "Доброе утро! :("
font = ImageFont.truetype("comic.ttf", size=200)
write_text.text((1537, 109), text, font=font)
gray_image.show()
print('--------------------------------ПОКАЗ ИЗОБРАЖЕНИЙ ЗАКОНЧЕН--------------------------------')
