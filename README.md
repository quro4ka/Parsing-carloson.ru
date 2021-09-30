# Parsing-carloson.ru
Collecting information about the car

# Parsing-carloson.ru
Parsing using the <b>requests</b> and <b>BeautifulSoup</b> library

You need to collect the following data:
  <ul><li>Name of the car</li></ul>
  <ul><li>Link to the car</li></ul>
  <ul><li>Specifications about the car</li></ul>
  <ul><li>Car image</li></ul>


<h1></h1>
<h1>How to use</h1>

1️⃣ Importing libraries

```python
import requests
from bs4 import BeautifulSoup
import csv
import os
```

`Requests makes a request to the server`

`BeautifulSoup allows you to transform a complex HTML document into a complex tree of various Python objects`

`A CSV file is a text file in which each line has several fields separated by commas, or other separators`

`The os module provides many functions for working with the operating system`



2️⃣ Declaring constants

```python
url = 'https://carloson.ru/car'
host = 'https://carloson.ru/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    '(KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.614 Yowser/2.5 Safari/537.36'
}
path = 'carloson.csv'
```
3️⃣ Declaring the get_html function

```python
def get_html(url):
    r = requests.get(url, headers=headers)
    return r
```
The function will return the value 200 if the request was executed successfully


4️⃣In the get_content() function, we create a soup object and collect the necessary page elements

```python
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='col-xl-4 col-lg-4 col-md-6 col-sm-6 col-12 mb-2 mb-md-4')
    cards = []
    for item in items:
         cards.append({
             'title': item.find('p', class_='two__block_slide__text__name').get_text().replace(' ', '').replace('\n', ''),
             'specifications': item.find('div', class_='two__block_slide__text__bottom').get_text().replace(' ', '').replace('\n', ' ').strip().replace('₽', 'Р'),
             'link': item.get('href'),
             'img': item.find('div', class_='img__box').find('img').get('data-src'),
         })

    return cards
```

5️⃣ We declare the main function parse(), in which we call all the functions

```python
def parse():
    html = get_html(url)
    if html.status_code == 200:
        cards = get_content(html.text)
        save_file(cards, path)
        os.startfile(path)
```

6️⃣Using the save_file() function, we save the data in CSV format
```python
def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Характеристики', 'Ссылка', 'Картинка'])
        for item in items:
            writer.writerow([item['title'], item['specifications'], item['link'], item['img']])
```


7️⃣ Calling the os.startfile(path) function with the path parameter

```python
os.startfile(path)
```

8️⃣ Calling the parse() function
```python
parse()
```






