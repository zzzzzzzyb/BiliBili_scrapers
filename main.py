#del 208171336

#check https://space.bilibili.com/1955897084 鸣潮

#check https://space.bilibili.com/23237718 害羞7

#check https://space.bilibili.com/216844 玩偶菌

#check https://space.bilibili.com/30131971 彩虹人

import re
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

columns = ['name', 'profile', 'fans', 'pros', 'plays', 'uid']
stat = pd.DataFrame(columns=columns)
stat.to_csv('stats.csv', index=False, header=True)
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Edge(options=option)

driver.get('https://space.bilibili.com/208171336')
sleep(10)
with open('links_1.txt', 'r', encoding='utf-8') as f:
    links = f.readlines()
    links = map(lambda x: x.replace("\n", ''), links)
    for link in links:
        stat = pd.DataFrame(columns=columns)
        driver.get(link + "/video")
        try:
            detail_div = WebDriverWait(driver, 5).until(
                lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/div'))
            name = detail_div.find_element(By.XPATH, './div[2]/div[1]/span[1]').text
            if "哔哩哔哩" in name:
                continue
            profile = detail_div.find_element(By.XPATH, './div[2]/div[2]/h4').get_attribute('title')
            # img_url = detail_div.find_element(By.XPATH, './div[1]/div[1]/div[1]/img').get_attribute('data-src')
            nums_div = WebDriverWait(driver, 5).until(
                lambda x: x.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[3]'))

            fans = nums_div.find_element(By.CSS_SELECTOR, '#navigator > div > div.n-inner.clearfix > div.n-statistics > a.n-data.n-fs').get_attribute('title')
            pros = nums_div.find_element(By.CSS_SELECTOR, '#navigator > div > div.n-inner.clearfix > div.n-statistics > div:nth-child(3)').get_attribute('title').split("获赞")[1]
            plays = nums_div.find_element(By.CSS_SELECTOR, '#navigator > div > div.n-inner.clearfix > div.n-statistics > div:nth-child(4)').get_attribute('title').split("总计为")[1]
            uid = link.split('/')[-1]
            currentRow = [name, profile, fans, pros, plays, uid]
            print(currentRow)
            stat.loc[len(stat)] = currentRow
            stat.to_csv('stats.csv', index=False, header=False,mode='a')
        except Exception as e:
            print(e)
            try:
                fans = nums_div.find_element(By.CSS_SELECTOR,
                                             '#navigator > div > div.n-inner.clearfix > div.n-statistics > div:nth-child(2)').get_attribute(
                    'title')
                pros = nums_div.find_element(By.CSS_SELECTOR,
                                             '#navigator > div > div.n-inner.clearfix > div.n-statistics > div:nth-child(3)').get_attribute(
                    'title').split("获赞")[1]
                plays = nums_div.find_element(By.CSS_SELECTOR,
                                              '#navigator > div > div.n-inner.clearfix > div.n-statistics > div:nth-child(4)').get_attribute(
                    'title').split("总计为")[1]
                currentRow = [name, profile, fans, pros, plays, uid]
                print(currentRow)
                stat.loc[len(stat)] = currentRow
                stat.to_csv('stats.csv', index=False, header=False, mode='a')
            except Exception as e1:
                print(e1)
                with open('errors.txt','a',encoding='utf-8') as f1:
                    f1.write(name+'\n')
            pass
        # url_list = []
        # try:
        #     total = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div/div[2]/div[4]/div/div/ul[3]/li[6]/a')
        #     print('text',total.text)
        #     number = re.findall(r"\d+", total.text)
        #     print('number',number)
        #     total = int(number[0])
        #     print('total',total)
        # except Exception as e:
        #     total = 3
        #     pass
        # for page in range(total):
        # while True:
        #     try:
        #         ul = WebDriverWait(driver, timeout=5).until(
        #             lambda x: x.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div/div[2]/div[4]/div/div/ul[2]'))
        #         lis = ul.find_elements(By.XPATH, "./li")
        #         for li in lis:
        #             if (str(li.get_attribute("data-aid"))) not in url_list:
        #                 url_list.append(str(li.get_attribute("data-aid")))
        #         driver.find_element(By.LINK_TEXT, '下一页').click()
        #         sleep(1)
        #     except Exception as e:
        #         print(e)
        #         break
        #
        #
        # print(len(url_list), url_list)
        # with open(f'./bv_list/{name}_bv_list.txt', 'a', encoding='utf-8') as f:
        #     for url in url_list:
        #         f.write(url + '\n')
        sleep(1.5)

