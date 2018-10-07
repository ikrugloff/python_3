"""
Функции ​к​лиента:​
- сформировать ​​presence-сообщение;
- отправить ​с​ообщение ​с​ерверу;
- получить ​​ответ ​с​ервера;
- разобрать ​с​ообщение ​с​ервера;
- параметры ​к​омандной ​с​троки ​с​крипта ​c​lient.py ​​<addr> ​[​<port>]:
- addr ​-​ ​i​p-адрес ​с​ервера;
- port ​-​ ​t​cp-порт ​​на ​с​ервере, ​​по ​у​молчанию ​​7777.
"""
import sys
import time
import threading
from socket import socket, AF_INET, SOCK_STREAM
from errors import UsernameToLongError, ResponseCodeLenError, MandatoryKeyError, ResponseCodeError
from config import *
from utils import send_message, get_message


def create_presence(account_name="Guest"):
    """
    Сформировать ​​presence-сообщение
    :param account_name: Имя пользователя
    :return: Словарь сообщения
    tests:
    ИЗ-ЗА времени трудно написать doctest
    """
    # Если имя не строка
    if not isinstance(account_name, str):
        # Генерируем ошибку передан неверный тип
        raise TypeError
    # Если длина имени пользователя больше 25 символов
    if len(account_name) > 25:
        # генерируем нашу ошибку имя пользователя слишком длинное
        raise UsernameToLongError(account_name)
    # формируем словарь сообщения
    message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    # возвращаем
    return message


def translate_response(response):
    """
    Разбор сообщения
    :param response: Словарь ответа от сервера
    :return: корректный словарь ответа
    """
    # Передали не словарь
    if not isinstance(response, dict):
        raise TypeError
    # Нету ключа response
    if RESPONSE not in response:
        # Ошибка нужен обязательный ключ
        raise MandatoryKeyError(RESPONSE)
    # получаем код ответа
    code = response[RESPONSE]
    # длина кода не 3 символа
    if len(str(code)) != 3:
        # Ошибка неверная длина кода ошибки
        raise ResponseCodeLenError(code)
    # неправильные коды символов
    if code not in RESPONSE_CODES:
        # ошибка неверный код ответа
        raise ResponseCodeError(code)
    # возвращаем ответ
    return response


def create_message(message_to, text, account_name='Guest'):
    return {ACTION: MSG, TIME: time.time(), TO: message_to, FROM: account_name, MESSAGE: text}


def read_messages(client):
    """
    Клиент читает входящие сообщения в бесконечном цикле
    :param client: сокет клиента
    """
    while True:
        # читаем сообщение
        message = get_message(client)
        print(message)


def write_messages(client, account_name):
    """Клиент пишет сообщение в бесконечном цикле"""
    while True:
        # Вводим сообщение с клавиатуры
        # Кому
        user_name = input('user: ')
        # Текст сообщения
        text = input('text: ')
        # Создаем jim сообщение
        message = create_message(user_name, text, account_name)
        # отправляем на сервер
        send_message(client, message)


if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    # Пытаемся получить параметры скрипта
    addr = DEFAULT_HOST
    port = DEFAULT_PORT
    # Логин пользователя
    account_name = input('Ваш login: ')
    # Соединиться с сервером
    client.connect((addr, port))
    # Создаем сообщение
    presence = create_presence(account_name)
    # Отсылаем сообщение
    send_message(client, presence)
    # Получаем ответ
    response = get_message(client)
    # Проверяем ответ
    response = translate_response(response)
    if response['response'] == OK:
        # в одном потоке слушаем сообщения
        reader = threading.Thread(target=read_messages, args=(client,))
        reader.start()

        # в главном потоке пишем сообщения
        write_messages(client, account_name)
