# Подключитесь к API НБУ ( документация тут https://bank.gov.ua/ua/open-data/api-dev ), получите текущий курс валют и запишите его в TXT-файл в таком формате:
#  "[дата создания запроса]"
# 1. [название ввалюты 1] to UAH: [значение курса к валюте 1]
# 2. [название ввалюты 2] to UAH: [значение курса к валюте 2]
# 3. [название ввалюты 3] to UAH: [значение курса к валюте 3]
# ...
# n. [название ввалюты n] to UAH: [значение курса к валюте n]

import requests
import json
import datetime

url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
response = requests.request('GET', url)
dt_now = datetime.datetime.now()
list = []
result_list = [str(dt_now)] #adding the current time to our list

for value in json.loads(response.text):
    list.append(value)

for num, item in enumerate(list):
    result_list.append((f"{num+1} {item['txt']} to UAH: {item['rate']} "))

result = '\n'.join(result_list)

with open('hw15.txt', 'w') as file:
    file.write(result)


