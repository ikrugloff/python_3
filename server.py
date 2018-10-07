import asyncio
from config import *
from utils import bytes_to_dict, dict_to_bytes
import time


class ChatServerProtocol(asyncio.Protocol):
    def __init__(self, connections):
        # Все подключения
        # 1.
        self.connections = connections

    def connection_made(self, transport):
        # 2. сохранение "сокет"
        self.transport = transport

    def connection_lost(self, exc):
        if isinstance(exc, ConnectionResetError):
            print('Обрыв соединения')
            del self.connections[self.transport]  # удаляем из соединений
        else:
            # почему то всегда None
            print(f'Ошибка при отключении клиента: {exc}')

    def data_received(self, data):
        """
        Вызов происходит если на сервер приходит сообщение
        3.
        """
        if data:
            # читаем данный из байтов
            message = bytes_to_dict(data)
            # смотрим что нам отправили
            print(f'Входящее сообщение: {message}')
            # обрабатываем
            self.message_handle_router(message)

    def message_handle_router(self, message):
        """
        Распределятор сообщений по обработчикам.
        параметром принимат JIM сообщение
        """
        # смотрим тим сообщения
        action = message[ACTION]
        if action == PRESENCE:
            self.presence_handle(message)
        elif action == MSG:
            self.new_msg_handle(message)
        elif action == GET_CONTACTS:
            pass
        elif action == ADD_CONTACT:
            pass
        elif action == DEL_CONTACT:
            pass
        else:
            self.send_error_message('Формат сообщения не распознан сервером!. Сообщение: {}'.format(message))

    def send_error_message(self, text):
        """
        Отправляет клиенту сообщение об ошибке
        """
        response = {RESPONSE: WRONG_REQUEST, ALERT: text}
        # self.transport - это наш канал общения с текущим клиентом
        self.transport.write(dict_to_bytes(response))

    def presence_handle(self, message):
        """
        Обработчик presence
        """
        # получаем имя пользователя
        account_name = message[USER][ACCOUNT_NAME]
        # формируем ответ
        response = {RESPONSE: OK}
        # отправляем self.transport - это текущий клиент
        self.transport.write(dict_to_bytes(response))
        # добавляем клиента в соединения
        # добавляем клиента в текущие соединения, его как ключ и его имя значением
        self.connections[self.transport] = account_name

    def is_client_online(self, account_name):
        """
        Проверяем наличие клиента в сети
        :param account_name:
        :return:
        """
        # Имя клиента должно быть в списке подключений
        if account_name in self.connections.values():
            return True
        else:
            return False

    def new_msg_handle(self, message):
        """
        Обработка сообщений пользователей
        """
        # текст сообщения
        body = message[MESSAGE]
        # от кого
        from_ = message[FROM]
        to = message[TO]

        # обработка сообщений.
        if self.is_client_online(to):
            for transport, account_name in self.connections.items():
                # Перебираем все подключения.
                # Если один и тот же клиент будет сидеть с разных клиентов,
                # он получит свое сообщение на все клиенты
                if account_name == to:
                    # Формирует сообщение для отправки с сервера
                    response = {ACTION: MSG, TIME: time.time(), TO: account_name, FROM: from_, MESSAGE: body}
                    # Отправляем
                    transport.write(dict_to_bytes(response))
        else:
            # Отправляем что клиента нету в сети
            response = {RESPONSE: BASIC_NOTICE, ALERT: 'Клиента нет в сети'}
            self.transport.write(dict_to_bytes(response))


if __name__ == "__main__":
    server_connections = {}  # клиенты

    loop = asyncio.get_event_loop()
    coro = loop.create_server(lambda: ChatServerProtocol(server_connections), DEFAULT_HOST, DEFAULT_PORT)
    server = loop.run_until_complete(coro)
    loop.run_forever()
