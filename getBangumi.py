from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Edge(options=option)
columns = ['cover_url', 'name', 'tags', 'play', 'fans', 'danmaku', 'score', 'score_people', 'start_time', 'profile']
df = pd.DataFrame(columns = columns)
df.to_csv('new_bangumi.csv', index=False,header=True,encoding='utf-8')
page = 1

url = "https://www.bilibili.com/anime/index/?from_spmid=666.4.index.0#st=1&order=3&season_version=1&spoken_language_type=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&sort=0&page="
driver.get(url+str(page))
sleep(10)
while True:
    df = pd.DataFrame(columns=columns)
    driver.get(url+str(page))
    sleep(1)
    try:
        for li_num in range(1, 21):
            df = pd.DataFrame(columns=columns)
            li = WebDriverWait(driver, 5).until(
                lambda x: x.find_element(By.XPATH, f'//*[@id="app"]/div[2]/div[1]/ul[2]/li[{li_num}]'))
            driver.get(li.find_element(By.XPATH, './a[1]').get_attribute('href'))
            try:
                a = WebDriverWait(driver, 5).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div/a'))
            except Exception as e:
                print('fuck')
            driver.get(a.get_attribute('href'))
            sleep(2)
            cover_url = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div[1]/div[1]/img').get_attribute('src')
            div_detail = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div[2]')
            name = div_detail.find_element(By.XPATH, './div[1]/span[1]').text
            tag_list = div_detail.find_elements(By.XPATH, './div[1]/span[2]/span')
            tags = ','.join([tag.text for tag in tag_list])
            play_str = div_detail.find_element(By.XPATH, './div[2]/div[1]/span[1]/em').text
            if play_str[-1] == '万':
                play = int(float(play_str[:-1])*10000)
            elif play_str[-1] == '亿':
                play = int(float(play_str[:-1])*100000000)
            else:
                play = int(play_str)
            fans_str = div_detail.find_element(By.XPATH, './div[2]/div[1]/span[2]/em').text
            if fans_str[-1] == '万':
                fans = int(float(fans_str[:-1])*10000)
            else:
                fans = int(fans_str)
            danmaku_str = div_detail.find_element(By.XPATH, './div[2]/div[1]/span[3]/em').text
            if danmaku_str[-1] == '万':
                danmaku = int(float(danmaku_str[:-1])*10000)
            elif danmaku_str == '-':
                danmaku = 0
            elif danmaku_str[-1] == '亿':
                danmaku = int(float(danmaku_str[:-1])*100000000)
            else:
                danmaku = int(danmaku_str)
            try:
                score = div_detail.find_element(By.XPATH, './div[2]/div[2]/div[1]/div[1]').text
            except Exception as e:
                score = 0
                pass
            try:
                score = float(score)
            except ValueError:
                score = 0
            try:
                score_people = div_detail.find_element(By.XPATH, './div[2]/div[2]/div[1]/div[2]/div[1]').text[:-2]
            except Exception as e:
                score_people = 0
                pass
            try:
                score_people = int(score_people)
            except ValueError:
                score_people = 0
            start_time = div_detail.find_element(By.XPATH, './div[3]/span[1]').text
            profile = div_detail.find_element(By.XPATH, './div[4]/span[1]').text
            currentRow = [cover_url,name,tags,play,fans,danmaku,score,score_people,start_time,profile]
            df.loc[len(df)] = currentRow
            df.to_csv('new_bangumi.csv', index=False,header=False,mode='a')
            print([name,tags,play,fans,danmaku,score,score_people,start_time,profile])
            driver.back()
            sleep(0.5)
            driver.back()
        page += 1
        driver.find_element(By.LINK_TEXT, '下一页').click()
    except Exception as e:
        print(e)
        with open('error.log', 'a') as err:
            err.write(driver.current_url+'\n')

