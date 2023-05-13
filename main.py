import tkinter as tk #для пользовательского интерфейса
from tkinter import messagebox #блок с информацией

from time import sleep

import pandas as pd #для записи и чтения таблицы с данными

import requests as rq
from bs4 import BeautifulSoup as bs #библиотеки для парсинга данных

def parse_lenta_last(): #создаём функцию для парсинга. Всего таких функций - 9
    url = 'https://m.lenta.ru/parts/news/' #ссылка на сайт
    pattern_url = 'https://m.lenta.ru' #шаблон для записи ссылки на новость
    response = rq.get(url) #делаем запрос
    soup = bs(response.text, 'lxml')
    newss = soup.find_all('li', class_='parts-page__item') #ищем все элементы, в которых есть вся нужная нам
    # информация по каждой новости

    title_for_df = []
    time_for_df = []
    link_for_df = [] #пустые списки, которые будем заполнять для внесения в таблицу

    for news in newss: #проходимся по каждой новости из всех найденных
        tag_link = news.find('a', class_ = 'card-mini')
        link = tag_link['href'] #ссылка на новость
        title = news.find('div', class_ = 'card-mini__title').text #заголовок новости
        time = news.find('time', class_ = 'card-mini__date').text #время публикации

        title_for_df.append(title)
        time_for_df.append(time)
        link_for_df.append(pattern_url + link) #добавляем полученные данные в списки

    df = pd.DataFrame({'Title': title_for_df, 'Time': time_for_df, 'Link': link_for_df}) #формируем датасет для
    # хранения всех данных
    df.to_excel('./lenta_last.xlsx', index = False) #записываем датасет в файл excel

    sleep(1.5) #небольшая задержка для вывода окна о готовности
    messagebox.showinfo('Info', 'Данные получены.') #сообщаем, что данные получены

'''Все функции расписывать нет смысла, так как их 9, а механизм работы абсолютно одинаковый'''

def parse_lenta_sport():
    url = 'https://m.lenta.ru/rubrics/sport/'
    pattern_url = 'https://m.lenta.ru'
    response = rq.get(url)
    soup = bs(response.text, 'lxml')
    newss = soup.find_all('li', class_='tabloid__item _mini')

    title_for_df = []
    time_for_df = []
    link_for_df = []

    for news in newss:
        tag_link = news.find('a', class_='card-mini')
        link = tag_link['href']
        title = news.find('div', class_='card-mini__title').text
        time = news.find('time', class_='card-mini__date').text

        title_for_df.append(title)
        time_for_df.append(time)
        link_for_df.append(pattern_url + link)

    df = pd.DataFrame({'Title': title_for_df, 'Time': time_for_df, 'Link': link_for_df})
    df.to_excel('./lenta_sport.xlsx', index=False)

    sleep(1.5)
    messagebox.showinfo('Info', 'Данные получены.')

def parse_lenta_economy():
    url = 'https://m.lenta.ru/rubrics/economics/'
    pattern_url = 'https://m.lenta.ru'
    response = rq.get(url)
    soup = bs(response.text, 'lxml')
    newss = soup.find_all('li', class_='tabloid__item _mini')

    title_for_df = []
    time_for_df = []
    link_for_df = []

    for news in newss:
        tag_link = news.find('a', class_='card-mini')
        link = tag_link['href']
        title = news.find('div', class_='card-mini__title').text
        time = news.find('time', class_='card-mini__date').text

        title_for_df.append(title)
        time_for_df.append(time)
        link_for_df.append(pattern_url + link)

    df = pd.DataFrame({'Title': title_for_df, 'Time': time_for_df, 'Link': link_for_df})
    df.to_excel('./lenta_economy.xlsx', index=False)

    sleep(1.5)
    messagebox.showinfo('Info', 'Данные получены.')

def parse_rbk_last():
    url = 'https://www.rbc.ru/?ysclid=lhhgjmkhnx81460719'
    response = rq.get(url)
    soup = bs(response.text, 'lxml')
    newss = soup.find_all('div', class_ = 'main__feed')

    title_for_df = []
    time_for_df = []
    link_for_df = []

    for news in newss:
        tag_link = news.find('a', class_='main__feed__link')
        link = tag_link['href']
        title = news.find('span', class_='main__feed__title').text
        time = str(news.attrs['data-modif-date'])
        time = time[time.find(',') + 2 : time.find('+') - 1]

        title_for_df.append(title)
        time_for_df.append(time)
        link_for_df.append(link)

    df = pd.DataFrame({'Title': title_for_df, 'Date and Time': time_for_df, 'Link': link_for_df})
    df.to_excel('./rbc_last.xlsx', index=False)

    sleep(1.5)
    messagebox.showinfo('Info', 'Данные получены.')

def parse_rbk_sport():
    url = 'https://sportrbc.ru/?utm_source=topline'
    response = rq.get(url)
    soup = bs(response.text, 'lxml')
    newss = soup.find_all('a', class_ = 'item__link rm-cm-item-link js-rm-central-column-item-link ')

    title_for_df = []
    time_for_df = []
    link_for_df = []

    for news in newss:
        link = news['href']
        title = news.find('span', class_='item__title rm-cm-item-text js-rm-central-column-item-text').text

        title_for_df.append(title)
        time_for_df.append('No info')
        link_for_df.append(link)

    df = pd.DataFrame({'Title': title_for_df, 'Date and Time': time_for_df, 'Link': link_for_df})
    df.to_excel('./rbc_sport.xlsx', index=False)

    sleep(1.5)
    messagebox.showinfo('Info', 'Данные получены.')

def parse_rbk_economy():
    url = 'https://www.rbc.ru/economics/?utm_source=topline'
    response = rq.get(url)
    soup = bs(response.text, 'lxml')
    newss = soup.find_all('div', class_ = 'item__wrap l-col-center')

    title_for_df = []
    time_for_df = []
    link_for_df = []

    for news in newss:
        tag_link = news.find('a', class_='item__link rm-cm-item-link js-rm-central-column-item-link')
        link = tag_link['href']
        title = news.find('span', class_='item__title rm-cm-item-text js-rm-central-column-item-text').text
        time = news.find('span', class_='item__category').text

        title_for_df.append(title)
        time_for_df.append(time)
        link_for_df.append(link)

    df = pd.DataFrame({'Title': title_for_df, 'Date and Time': time_for_df, 'Link': link_for_df})
    df.to_excel('./rbc_economy.xlsx', index=False)

    sleep(1.5)
    messagebox.showinfo('Info', 'Данные получены.')

def parse_kommersant_last():
    url = 'https://www.kommersant.ru/lenta?from=all_lenta'
    pattern_url = 'https://www.kommersant.ru'
    response = rq.get(url)
    soup = bs(response.text, 'lxml')
    newss = soup.find_all('div', class_='rubric_lenta__item_text')

    title_for_df = []
    time_for_df = []
    link_for_df = []

    for news in newss:
        tag_link = news.find('a', class_ = 'uho__link--overlay')
        link = tag_link['href']
        title = news.find('a', class_ = 'uho__link--overlay').text
        time = news.find('p', class_ = 'rubric_lenta__item_tag').text

        title_for_df.append(title)
        time_for_df.append(time.strip())
        link_for_df.append(pattern_url + link)

    df = pd.DataFrame({'Title': title_for_df, 'Time': time_for_df, 'Link': link_for_df})
    df.to_excel('./kommersant_last.xlsx', index=False)

    sleep(1.5)
    messagebox.showinfo('Info', 'Данные получены.')

def parse_kommersant_sport():
    url = 'https://www.kommersant.ru/rubric/9?from=burger'
    pattern_url = 'https://www.kommersant.ru'
    response = rq.get(url)
    soup = bs(response.text, 'lxml')
    newss = soup.find_all('div', class_='uho__text rubric_lenta__item_text')

    title_for_df = []
    time_for_df = []
    link_for_df = []

    for news in newss:
        tag_link = news.find('a', class_ = 'uho__link uho__link--overlay')
        link = tag_link['href']
        title = news.find('a', class_ = 'uho__link uho__link--overlay').text
        time = news.find('p', class_ = 'uho__tag rubric_lenta__item_tag hide_mobile').text

        title_for_df.append(title)
        time_for_df.append(time.strip())
        link_for_df.append(pattern_url + link)

    df = pd.DataFrame({'Title': title_for_df, 'Time': time_for_df, 'Link': link_for_df})
    df.to_excel('./kommersant_sport.xlsx', index=False)

    sleep(1.5)
    messagebox.showinfo('Info', 'Данные получены.')

def parse_kommersant_economy():
    url = 'https://www.kommersant.ru/rubric/3?from=burger'
    pattern_url = 'https://www.kommersant.ru'
    response = rq.get(url)
    soup = bs(response.text, 'lxml')
    newss = soup.find_all('div', class_='uho__text rubric_lenta__item_text')

    title_for_df = []
    time_for_df = []
    link_for_df = []

    for news in newss:
        tag_link = news.find('a', class_ = 'uho__link uho__link--overlay')
        link = tag_link['href']
        title = news.find('a', class_ = 'uho__link uho__link--overlay').text
        time = news.find('p', class_ = 'uho__tag rubric_lenta__item_tag hide_mobile').text

        title_for_df.append(title)
        time_for_df.append(time.strip())
        link_for_df.append(pattern_url + link)

    df = pd.DataFrame({'Title': title_for_df, 'Time': time_for_df, 'Link': link_for_df})
    df.to_excel('./kommersant_economy.xlsx', index=False)

    sleep(1.5)
    messagebox.showinfo('Info', 'Данные получены.')

def window_of_parser(): #функция для вызова пользовательского интерфейса
    window = tk.Tk()
    window.title("Новости") #устанавливаем заголовок окна
    window.geometry('640x480') #задаём размеры окна

    '''задаём надписи, которые означают источник, с которого будут парситься данные'''
    p_rbk = tk.Label(window, text="РБК", font=("Arial Bold", 20)) #задаём текст, а также шрифт и размер
    p_rbk.grid(column=0, row=0, padx=15, pady=10) #задаём расположение
    p_lenta = tk.Label(window, text="Лента", font=("Arial Bold", 20))
    p_lenta.grid(column=1, row=0, padx=15, pady=10)
    p_komer = tk.Label(window, text="Коммерсантъ", font=("Arial Bold", 20))
    p_komer.grid(column=2, row=0, padx=15, pady=10)

    '''далее прописываются все кнопки для парсинга'''
    btn_rbk_last = tk.Button(window, text="Последние", font=("Arial", 15), command=parse_rbk_last) #текст,
    # шрифт и размер кнопки. Также указываем функцию, которая будет отрабатывать при нажатии на данную кнопку
    btn_rbk_last.grid(column=0, row=1, padx=15, pady=5) #задаём расположение кнопки

    btn_lenta_last = tk.Button(window, text="Последние", font=("Arial", 15), command=parse_lenta_last)
    btn_lenta_last.grid(column=1, row=1, padx=15, pady=5)

    btn_komer_last = tk.Button(window, text="Последние", font=("Arial", 15), command=parse_kommersant_last)
    btn_komer_last.grid(column=2, row=1, padx=15, pady=5)

    btn_rbk_sport = tk.Button(window, text="Спорт", font=("Arial", 15), command=parse_rbk_sport)
    btn_rbk_sport.grid(column=0, row=2, padx=15, pady=5)

    btn_lenta_sport = tk.Button(window, text="Спорт", font=("Arial", 15), command=parse_lenta_sport)
    btn_lenta_sport.grid(column=1, row=2, padx=15, pady=5)

    btn_komer_sport = tk.Button(window, text="Спорт", font=("Arial", 15), command=parse_kommersant_sport)
    btn_komer_sport.grid(column=2, row=2, padx=15, pady=5)

    btn_rbk_economy = tk.Button(window, text="Экономика", font=("Arial", 15), command=parse_rbk_economy)
    btn_rbk_economy.grid(column=0, row=3, padx=15, pady=5)

    btn_lenta_economy = tk.Button(window, text="Экономика", font=("Arial", 15), command=parse_lenta_economy)
    btn_lenta_economy.grid(column=1, row=3, padx=15, pady=5)

    btn_komer_economy = tk.Button(window, text="Экономика", font=("Arial", 15), command=parse_kommersant_economy)
    btn_komer_economy.grid(column=2, row=3, padx=15, pady=5)

    window.mainloop() #открываем окно пользовательского интерфейса

window_of_parser() #вызываем функцию, которая создаст и откроет пользовательский интерфейс
