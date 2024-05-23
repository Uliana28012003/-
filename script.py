import requests  # Модуль для выполнения HTTP-запросов
import concurrent.futures  # Модуль для работы с параллелизмом

def send_request(url):
    response = requests.get(url)  # Выполнение GET-запроса к указанному URL
    print(response.text)  # Вывод текста ответа

urls = ['http://127.0.0.1:25566'] * 1  # Список URL для запросов
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(send_request, urls)  # Параллельное выполнение функции send_request для каждого URL из списка

