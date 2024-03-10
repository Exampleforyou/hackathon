import os

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def save_text(url, output_file):
    try:
        # Создаем объект UserAgent для генерации фейкового юзер-агента
        ua = UserAgent()

        # Заголовки запроса с фейковым юзер-агентом
        headers = {'User-Agent': ua.random, 'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'TE': 'Trailers'}

        # Отправляем GET-запрос на указанный URL с заданными заголовками
        response = requests.get(url, headers=headers)

        # Проверяем успешность запроса (код 200)
        if response.status_code == 200:
            # Используем BeautifulSoup для парсинга HTML и извлечения текста
            soup = BeautifulSoup(response.text, 'html.parser')
            text_content = soup.get_text()

            # Сохраняем текстовую информацию в файл
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(text_content)
            print(f'Текст успешно сохранен в файл {output_file}')
        else:
            print(f'Ошибка при получении страницы. Код состояния: {response.status_code}')

    except Exception as e:
        print(f'Произошла ошибка: {e}')


    except Exception as e:
        print(f'Произошла ошибка: {e}')

# Пример использования
tmp = 1
#url_to_scrape = f'https://www.cbr.ru/faq/bank_s/'
url_to_scrape = f'https://www.cbr.ru/faq/w_fin_sector/Transgranichnie_perevodi/'

download_path = "faq\\w_fin_sector\\Transgranichnie_perevodi"

try:
    os.mkdir(download_path)
except:
    pass
filename = f"{tmp}" + ".txt"
output_file_path = os.path.join(download_path, filename)
save_text(url_to_scrape, output_file_path)
with open(os.path.join(download_path,"!links.txt"), 'w', encoding='utf-8') as file:
    file.write(url_to_scrape)
    print(url_to_scrape)
