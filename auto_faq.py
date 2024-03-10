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
            with open(output_file, 'w+', encoding='utf-8') as file:
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
urls = [

    "https://www.cbr.ru/explan/support_measures",
    "https://www.cbr.ru/banking_sector/explan/order_reflection_investments_credit_org",
    "https://www.cbr.ru/RSCI/expl_market_part/other",
    "https://www.cbr.ru/RSCI/expl_market_part/pension_funds",
    "https://www.cbr.ru/RSCI/expl_market_part/spec_dep",
    "https://www.cbr.ru/RSCI/expl_market_part/managment",
    "https://www.cbr.ru/admissionfinmarket/exlpain/dopusk_npf",
    "https://www.cbr.ru/insurance/explained/mery-podderzhki-strakhovogo-sektora-v-t-ch-primenenie-informacionnogo-pis-ma-banka-rossii-ot-25-02-2022-in-18-53-16-",
    "https://www.cbr.ru/insurance/explained/other",
    "https://www.cbr.ru/insurance/explained/lic",
    "https://www.cbr.ru/insurance/explained/authorized_capital",
    "https://www.cbr.ru/insurance/explained/coordination_appointment",
    "https://www.cbr.ru/insurance/explained/626-p",
    "https://www.cbr.ru/insurance/explained/finstab_ssd",
    "https://www.cbr.ru/insurance/explained/5968_u",
    "https://www.cbr.ru/insurance/explained/raschet-strakhovykh-rezervov-primenenie-polozheniya-banka-rossii-ot-16-11-2021-781-p-o-trebovaniyakh-k-finansovoy-ustoychivosti-i-platezhesposobnosti-strakhovschikov-",
    "https://www.cbr.ru/insurance/explained/6139-u",
    "https://www.cbr.ru/insurance/explained/781-p",
    "https://www.cbr.ru/projects_xbrl/explan/other",
    "https://www.cbr.ru/projects_xbrl/explan/programmnoe-obespechenie-konverter-i-anketa-redaktor-xbrl-",
    "https://www.cbr.ru/issuers_corporate/explan/securities_credit",
    "https://www.cbr.ru/securities_market/explan/issuing_opinion",
    "https://www.cbr.ru/securities_market/explan/acquisition_30",
    "https://www.cbr.ru/explan/macro_limit",
    "https://www.cbr.ru/explan/form_0420833",
    "https://www.cbr.ru/microfinance/explan/micro",
    "https://www.cbr.ru/microfinance/explan/kpk",
    "https://www.cbr.ru/microfinance/explan/lombard",
    "https://www.cbr.ru/microfinance/explan/skpk",
    "https://www.cbr.ru/microfinance/explan/zhnk",
    "https://www.cbr.ru/microfinance/explan/rpdn",
    "https://www.cbr.ru/microfinance/explan/calc_res",
    "https://www.cbr.ru/explan/mfo_calc",
    "https://www.cbr.ru/explan/oper_br/om_dm",
    "https://www.cbr.ru/explan/oper_br/reserve_requirements",
    "https://www.cbr.ru/microfinance/explan/reporting_other/",
    "https://www.cbr.ru/microfinance/explan/reporting_micro",
    "https://www.cbr.ru/microfinance/explan/reporting_kpk",
    "https://www.cbr.ru/microfinance/explan/reporting_lombard",
    "https://www.cbr.ru/explan/ssd",
    "https://www.cbr.ru/explan/inv_platform",

]
for url_to_scrape in urls:
    #rl_to_scrape = f'https://www.cbr.ru/faq/w_fin_sector/Transgranichnie_perevodi/'

    url_to_scrape.rfind('/')
    download_path = f"auto_faq\\{url_to_scrape[url_to_scrape.rfind('/')+1:]}"

    try:
        os.mkdir(download_path)
    except:
        pass
    filename = f"{tmp}" + ".txt"
    output_file_path = os.path.join(download_path, filename)
    save_text(url_to_scrape, output_file_path)
    with open(os.path.join(download_path,"!links.txt"), 'w+', encoding='utf-8') as file:
        file.write(url_to_scrape)
        print(url_to_scrape)
