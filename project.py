"""
Ваша задача — написать код, который будет
запрашивать у Балабобы (https://yandex.ru/lab/yalm - генератор текстов) список жанров с их id, разбирать его и печатать в консоли;
отправлять Балабобе ключевую фразу и id жанра, получать ответ Балабобы, разбирать его и печатать в консоли.
Ответы Балабобы приходят в формате JSON, они конвертируются в Python-словари с помощью метода json().
"""


import requests
# Переменные query и genre - это параметры для POST-запроса.
# query - ключевая фраза для запроса к Балабобе

query = 'Рыбы'
# числовое значение (id жанра) в переменной genre
genre = 11

def get_genres():
    """
    Функция отправляет запрос к Балабобе,
    и получает в ответ список жанров.
    """
    genres_url = 'https://zeapi.yandex.net/lab/api/yalm/intros'
    # Обернём выполнение и обработку запроса в блок try/except,
    # чтобы в случае ошибки выполнение программы не прервалось
    # и вернулся пустой список genres_list
    try:
        response = requests.get(genres_url)
        response = response.json()
        # в переменной genres_list сохраним список жанров
        genres_list = response['intros']
    except:
        # В случае ошибки
        print('Во время выполнения функции get_genres() возникла ошибка!')
        genres_list = []
    return genres_list


def print_genres(genres_list):
    """
    Печатает в форматированном виде список доступных жанров,
    полученный из функции get_genres()
    genres: ответ от функции get_genres(), который нужно распечатать
    """
    print("Список жанров, в которых можно продолжить фразу:")
    for genre in genres_list:
        print(genre[0], '-', genre[1], '-', genre[2])


def generate_text(query, genre):
    """
    Функция отправляет POST-запрос к Балабобе,
    и получает ответ в виде словаря.
    Параметры POST-запроса:
    query: ключевая фраза
    genre: id жанра, в котором Балабоба должен сгенерировать текст
    """
    text_url = 'https://zeapi.yandex.net/lab/api/yalm/text3'
    # Параметры запроса для Балабобы храним в словаре data.
    # в элементе с ключом query значение переменной, содержащей ключевую фразу,
    # а в элементе с ключом intro - переменная, хранящая id жанра
    data = {
        "query": query,
        "intro": genre
    }
    try:
        response = requests.post(url=text_url, json=data)
        print(response) 
    
    # значение переменной response преобразуем в Python-словарь
    # и сохраним этот словарь в переменную dict_response
        dict_response = response.json()
    except:
        print('Во время выполнения функции generate_text() возникла ошибка!')
        dict_response = {}
    return dict_response


def print_text(text_dict):
    """
    Печатает текст ответа в форматированном виде.
    dict_response: ответ на запрос в виде словаря
    """
    print('\n' + 'Ответ на ваш запрос:' + '\n')
    # В словаре text_dict под ключом query хранится ключевая фраза,
    # а под ключом text - текст, сгенерированный Балабобой.
    print(text_dict['query'], text_dict['text'])


# Вызов функций: получаем и печатаем жанры
# Получаем список доступных жанров, используя функцию get_genres() 
# и записываем его в genres_list
genres_list = get_genres()
# Выводим жанры в читабельном виде, используя функцию print_genres()
print_genres(genres_list)

# Вызов функций: получаем и печатаем сгенерированный текст
# Передаем параметры для запроса к Балабобе и сохраняем ответ в переменной text_dict
text_dict = generate_text(query, genre)
# Преобразуем и выводим ответ при помощи функции print_text()
print_text(text_dict)