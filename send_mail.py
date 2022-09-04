from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText  # Текст/HTML
import smtplib

from jinja2 import Environment, FileSystemLoader  # Подгрузка шаблона
import os

env = Environment(
    loader=FileSystemLoader('%s/static/' % os.path.dirname(__file__)))

# # Create a MIMEText object to contains the email Html content. There is also an image in the Html content. The image cid is image1.
# msgText = MIMEText('<b>This is the <i>HTML</i> content of this email</b> it contains an image.<br><img src="cid:image1"><br>', 'html')
# # Attach the above html content MIMEText object to the msgAlternative object.
# msgAlternative.attach(msgText)
#
# # Open a file object to read the image file, the image file is located in the file path it provide.
# fp = open('/usr/var/test.jpg', 'rb')
# # Create a MIMEImage object with the above file object.
# msgImage = MIMEImage(fp.read())
# # Do not forget close the file object after using it.
# fp.close()
#
# # Add 'Content-ID' header value to the above MIMEImage object to make it refer to the image source (src="cid:image1") in the Html content.
# msgImage.add_header('Content-ID', '<image1>')
# # Attach the MIMEImage object to the email body.
# msgRoot.attach(msgImage)

def send_monitoring_report(metrics_data):
    user = "scoring-support"  # Пользователь
    password = "edD@fghHg5%t456"  # Пароль

    addr_from = "ScoringSupport@skgelios.ru"  # Адресат
    test_addr_to = ["akharlamov@mind-set.ru"]  # Получатель для тестирования
    addr_to = ["gelios_tech@mind-set.ru", "n.kalashnikov@skgelios.ru", "dima@mind-set.ru", "frank@mind-set.ru",
               "akharlamov@mind-set.ru"]  # Получатели

    msg = MIMEMultipart()  # Создаем сообщение
    msg['From'] = "ScoringSupport@skgelios.ru"  # Адресат
    msg['To'] = addr_to  # Получатель
    msg['Subject'] = "Отчёт мониторинга системы"  # Тема сообщения

    template = env.get_template('hey.html')  # Получаем шаблон для отправки
    body = template.render(all_metrics=metrics_data[0],
                           percentage_s=round(metrics_data[5]),
                           percentage_f=round(metrics_data[4]),
                           total_requests=metrics_data[3],
                           failed_requests=metrics_data[2],
                           success_requests=metrics_data[1])  # Наполнение шаблона метриками

    msg.attach(MIMEText(body, 'html'))  # Добавляем в сообщение текст

    server = smtplib.SMTP('mail.ins.ru', 25)  # Создаем объект SMTP
    server.starttls()  # Начинаем шифрованный обмена по TLS
    server.login(user, password)  # Получаем доступ
    server.sendmail(addr_from, test_addr_to, msg.as_string())  # Отправляем сообщение
    server.quit()
