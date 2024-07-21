from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Edge(options=option)

driver.get('https://www.bilibili.com/v/popular/rank/all')
postfix_list = ['all', 'guochan', 'douga', 'music', 'dance', 'game', 'knowledge', 'tech', 'sports', 'car', 'life', 'food', 'animal', 'kichiku', 'fashion', 'ent', 'cinephile', 'origin', 'rookie']

for postfix in postfix_list:
    if postfix == 'all':
        continue
    driver.get(f'https://www.bilibili.com/v/popular/rank/{postfix}')
    sleep(2)
    ul = WebDriverWait(driver, timeout=10).until(lambda x: x.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/ul'))
    lis = ul.find_elements(By.XPATH, './li')
    bv_list = []
    for li in lis:
        bv = li.find_element(By.XPATH, './div[1]/div[2]/a').get_attribute('href').split('/')[-1]
        bv_list.append(bv)
    print(bv_list)
    if postfix == 'all':
        filename = './popular/全站.txt'
    else:
        filename = f'./popular/{postfix}.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        for bvs in bv_list:
            f.write(bvs + '\n')


