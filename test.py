import json
import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as Bs

options = webdriver.ChromeOptions()
ua = UserAgent()
options.add_argument('--headless')
options.add_argument(f'user-agent={ua.chrome}')
options.add_argument('--disable-blink-features=AutomationControlled')


# URL = 'https://www.google.com/maps/search/%D1%8F%D0%B7%D1%8B%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5+%D0%BA%D1%83%D1%80%D1%81%D1%8B+%D0%B2+%D0%91%D0%B8%D1%88%D0%BA%D0%B5%D0%BA%D0%B5/@42.8760111,74.5856421,14z/data=!3m1!4b1'


def get_courses(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(2)
    courses_list = driver.find_elements(By.CLASS_NAME, value='Nv2PK')

    while True:
        ActionChains(driver).move_to_element(courses_list[-1]).perform()

        # скроллит список до конца
        last_review = courses_list[-1]
        driver.execute_script('arguments[0].scrollIntoView(true);', last_review)

        courses_list = driver.find_elements(By.CLASS_NAME, value='Nv2PK')
        if last_review == courses_list[-1]:
            return driver.page_source
        time.sleep(2)


def get_soup(html):
    soup = Bs(html, 'lxml')
    return soup


exc = ['открыто', 'закрыто', 'проложить маршрут']


def get_data(soup):
    courses_list = soup.find_all('div', class_='Nv2PK')
    data = []
    for course in courses_list:
        link_div = course.find('div', class_='kdfrQc')
        link_div = link_div.find('a', class_='lcr4fd')
        if link_div:
            link = link_div.get('href').replace('/url?q=', '')
        else:
            link = course.find('a', class_='hfpxzc').get('href')
        text = course.text.split()
        text = ' '.join([i for i in text if i])
        text = text.split('·')
        res = []
        for i in text:
            if any(one_exc in i.lower() for one_exc in exc[:-1]):
                continue
            if exc[-1] in i.lower():
                tel_number = ''
                for letter in i:
                    if letter.isdigit():
                        tel_number += letter
                i = f'Номер телефона: {tel_number}'

            res.append(i.strip())

        data.append('\n'.join(res) + f'\n{link.strip()}')

    return data


# def main():
#     html = get_courses(url=URL)
#     soup = get_soup(html)
#     data = get_data(soup)
#
# # bot.send_mail(chat_id, data)
#
#
# if __name__ == '__main__':
#     main()
