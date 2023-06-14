import requests  # библиотека для запросов
from fake_useragent import UserAgent  # библиотека для получения хедеров чтоб сайт не посчитал нас ботом
from bs4 import BeautifulSoup  # библиотека для парсинга


def parse_recipe(url):  # функция, которая получает url сайта и возвращает рецепт
    header = {'User-Agent': UserAgent().random}  # генерируем рандомный хедер

    page = requests.get(url, headers=header)  # отправляем запрос
    soup = BeautifulSoup(page.content, 'html.parser')  # получаем html

    recipe = soup.find(class_='steps').find_all('li')  # фильтруем нужные теги
    text_recipe = ''  # переменная для записи текста
    j = 1  # переменная для выделения пунктов в рецепте
    for i in recipe:  # цикл, который бежит по массиву recipe и достаёт текст
        text_recipe += str(j) + '. ' + i.text + '\n'  # формируем нужную нам запись
        j += 1
    return text_recipe
