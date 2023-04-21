from selenium.webdriver.common.by import By 
import undetected_chromedriver as uc 


URL='https://www.avito.ru/moskva/odezhda_obuv_aksessuary/obuv_muzhskaya/' \
    'krossovki-ASgBAgICAkTeArqp1gLOvQ68nJQC' \
    '?f=ASgBAQICAkTeArqp1gLOvQ68nJQCAkDivA0k7tE0uqvWAriHDjTg8pMB3vKTAdzykwE' \
    '&q=brooks' \
    '&s=104'
CHROME_VER = 110


options = uc.ChromeOptions() 
options.add_argument('--headless')
driver = uc.Chrome(version_main=CHROME_VER, options=options) 


def main():
    datalist = []
    driver.get(URL)
    titles = driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
    for title in titles:
        name = title.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
        description = title.find_element(By.CSS_SELECTOR, "[class*='item-description']").text
        url = title.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute("href")
        price = title.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute("content")
        data = {
            'name': name,
            'description': description,
            'url': url,
            'price': price
        }
        if price != None and int(price) <= 10000:
            datalist.append(data)
            print(data)
    return datalist


if __name__ == '__main__':
    main()
    