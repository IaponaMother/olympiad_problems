from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import numpy as np

from openpyxl import load_workbook


Year = 1999
city = '4368'

headers = requests.utils.default_headers()
headers.update({'User-Agent': 'My User Agent'})


def graph(wind_speed, path):
  x = np.array([day for day in range(365)])
  y = np.array(wind_speed)

  plt.figure(figsize=(12, 8))
  plt.plot(x, y)
  plt.savefig(path + '.jpg')

def parse(url):
  wind = []

  for month in range(1, 13):
    response = requests.get(url + str(month) + '/', headers=headers)
    soup = BeautifulSoup(response.text, features="lxml")
    span = soup.find_all('span')

    span = span[::2]
    l = len(span)
    if month == 2:
      count = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
      count = 30
    else:
      count = 31

    if l < count:
      for j in range(count - l):
        span.append(1)

    elif l > count:
      span.pop()



    for item in span:
      if 'Ш' in str(item):
        wind.append(0)
      elif item == 1:
        wind.append(1)

      else:
        item.img.decompose()
        item.img.decompose()
        item.br.decompose()
        i = str(item)[8:-10]
        if " " in i:
          i = i[1:]
        wind.append(int(i))
  return wind

for year in range(1998, 2022):
  graph(parse('https://www.gismeteo.ru/diary/4079/' + str(year) + '/'), 'figure_' + str(year))





# table_path = 'wind_speed.xlsx'
# workbook = load_workbook(table_path)
# table = workbook['Лист1']
# alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#
# def create_table(year1, year2):
#   n = 0
#   for year in range(year1, year2 + 1):
#     table[alf[n] + '1'] = year
#     workbook.save(table_path)
#     arr = parse('https://www.gismeteo.ru/diary/4368/' + str(year) + '/')
#     graph(arr)
#     for i in range(365):
#       num = alf[n] + str(i+2)
#       table[num] = arr[i]
#       workbook.save(table_path)
#     n += 1

#
# workbook.close()
