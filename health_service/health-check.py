"""Health-check microservice.
Run it together with the main service."""
import os
import signal
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.error import HTTPError

from flask import Flask

import requests

import threading

app = Flask(__name__)

url = 'http://192.168.0.169:5000/healthcheck'
counter = 0

user = "scoring-support"
password = "edD@fghHg5%t456"
addr_from = "ScoringSupport@skgelios.ru"
addr_to = ['akharlamov@mind-set.ru']


# 'n.kalashnikov@skgelios.ru', 'a.komarov@skgelios.ru

def send_email():
    """Send service health failed email."""
    msg = MIMEMultipart()  # Создаем сообщение

    # Тестовая отправка разработчику
    # addr_to = 'akharlamov@mind-set.ru'  # Получатель для тестирования
    # msg['To'] = addr_to  # Получатель для тестирования

    msg['From'] = addr_from
    msg['To'] = ", ".join(addr_to)
    msg['Subject'] = "Отчет работоспособности сервиса"

    msg = MIMEMultipart()  # Создаем сообщение
    msg['From'] = addr_from
    msg['To'] = ", ".join(addr_to)
    msg['Subject'] = "Ошибка"

    body = 'Cервис завершил свою работу'
    msg.attach(MIMEText(body, 'plain'))  # Добавляем в сообщение текст

    server = smtplib.SMTP('mail.ins.ru', 25)  # Создаем объект SMTP

    server.starttls()  # Начинаем шифрованный обмена по TLS
    server.login(user, password)  # Получаем доступ
    server.send_message(msg)  # Отправляем сообщение
    server.quit()


def send_tg_message():
    """Send service health failed tg message."""
    pass


def shutdown():
    return os.kill(os.getpid(), signal.SIGINT)


def health():
    """Ping main service health-check every 5 sec."""
    global counter

    t = threading.Timer(5.0, health)
    t.start()

    try:
        requests.get(url, timeout=1)
    except Exception:
        print('Ошибка, повтор запроса')
        counter += 1
        if counter == 3:
            t.cancel()
            send_email()
            send_tg_message()
            shutdown()


health()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2007)
