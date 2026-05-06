from selenium import webdriver
import time
import pandas as pd
import threading

toplist = [0] * 150  # 游戏排名
namelist = [0] * 150  # 游戏名称
firmlist = [0] * 150  # 厂商名称
scorelist = [0] * 150  # 游戏评分
categorylist = [0] * 150  # 游戏分类
taglist = [0] * 150  # 游戏标签
statisticslist = [0] * 150  # 数据(关注、下载、购买)
games = list()

# 配置，防止“不安全”
option = webdriver.ChromeOptions()
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option('excludeSwitches', ['enable-automation'])

lock = threading.Lock()


def gettable(n, driver):  # 第n页
    # 获得游戏排名
    top_content = driver.find_elements_by_xpath('//*[@id="topList"]/div/span[2]')
    for i in range(0, 30):
        toplist[((n - 1) * 30 + i)-150] = top_content[(n - 1) * 30 + i].text
    # 获得游戏名称
    name_content = driver.find_elements_by_xpath('//*[@id="topList"]/div/div[3]/a/h4')
    for i in range(0, 30):
        namelist[((n - 1) * 30 + i)-150] = name_content[(n - 1) * 30 + i].text
    # 获得厂商名称
    firm_content = driver.find_elements_by_xpath('//*[@id="topList"]/div/div[3]/p[1]/a')
    for i in range(0, 30):
        firmlist[((n - 1) * 30 + i)-150] = firm_content[(n - 1) * 30 + i].text
    # 获得游戏评分
    score_content = driver.find_elements_by_xpath('//*[@id="topList"]/div/div[3]/div[1]/p/span')
    for i in range(0, 30):
        scorelist[((n - 1) * 30 + i)-150] = score_content[(n - 1) * 30 + i].text
    # 获得游戏分类
    category_content = driver.find_elements_by_xpath('//*[@id="topList"]/div/div[3]/div[3]/a')
    for i in range(0, 30):
        categorylist[((n - 1) * 30 + i)-150] = category_content[(n - 1) * 30 + i].text
    # 获得游戏标签
    tag_content = driver.find_elements_by_xpath('//*[@id="topList"]/div/div[3]/div[2]')
    for i in range(0, 30):
        taglist[((n - 1) * 30 + i)-150] = tag_content[(n - 1) * 30 + i].text.replace('\n', ',')


def getpage(n, driver):
    for i in range(1, n):
        search_button = driver.find_element_by_xpath('//*[@id="page-top"]/section[5]/button')
        search_button.click()
        time.sleep(3)


def getstatistics(n, driver):  # 获得第n页的游戏数据
    links = driver.find_elements_by_xpath('//*[@id="topList"]/div/div[3]/a')
    for i in range(0, 6):  # 分为六组，每五个为一组获取
        driver2 = webdriver.Chrome(chrome_options=option)
        driver2.get(links[(n - 1) * 30 + i * 5].get_attribute('href'))
        driver3 = webdriver.Chrome(chrome_options=option)
        driver3.get(links[(n - 1) * 30 + i * 5 + 1].get_attribute('href'))
        driver4 = webdriver.Chrome(chrome_options=option)
        driver4.get(links[(n - 1) * 30 + i * 5 + 2].get_attribute('href'))
        driver5 = webdriver.Chrome(chrome_options=option)
        driver5.get(links[(n - 1) * 30 + i * 5 + 3].get_attribute('href'))
        driver6 = webdriver.Chrome(chrome_options=option)
        driver6.get(links[(n - 1) * 30 + i * 5 + 4].get_attribute('href'))
        # 获得下载次数
        statistics_content = driver2.find_elements_by_xpath('//*[@id="js-nav-sidebar-main"]/div[1]/div/div/section[1]/div[1]/div[2]/div[2]/div[1]/div/p')
        for statistics in statistics_content:
            statisticslist[((n - 1) * 30 + (i - 1) * 5)-150] = statistics.text
        driver2.close()
        statistics_content = driver3.find_elements_by_xpath('//*[@id="js-nav-sidebar-main"]/div[1]/div/div/section[1]/div[1]/div[2]/div[2]/div[1]/div/p')
        for statistics in statistics_content:
            statisticslist[((n - 1) * 30 + (i - 1) * 5 + 1)-150] = statistics.text
        driver3.close()
        statistics_content = driver4.find_elements_by_xpath('//*[@id="js-nav-sidebar-main"]/div[1]/div/div/section[1]/div[1]/div[2]/div[2]/div[1]/div/p')
        for statistics in statistics_content:
            statisticslist[((n - 1) * 30 + (i - 1) * 5 + 2)-150] = statistics.text
        driver4.close()
        statistics_content = driver5.find_elements_by_xpath('//*[@id="js-nav-sidebar-main"]/div[1]/div/div/section[1]/div[1]/div[2]/div[2]/div[1]/div/p')
        for statistics in statistics_content:
            statisticslist[((n - 1) * 30 + (i - 1) * 5 + 3)-150] = statistics.text
        driver5.close()
        statistics_content = driver6.find_elements_by_xpath('//*[@id="js-nav-sidebar-main"]/div[1]/div/div/section[1]/div[1]/div[2]/div[2]/div[1]/div/p')
        for statistics in statistics_content:
            statisticslist[((n - 1) * 30 + (i - 1) * 5 + 4)-150] = statistics.text
        driver6.close()


class getpage6(threading.Thread):
    def run(self):
        driver06 = webdriver.Chrome(chrome_options=option)
        driver06.get('https://www.taptap.com/top/ios/played')
        getpage(6, driver06)
        gettable(6, driver06)
        getstatistics(6, driver06)


class getpage7(threading.Thread):
    def run(self):
        driver07 = webdriver.Chrome(chrome_options=option)
        driver07.get('https://www.taptap.com/top/ios/played')
        getpage(7, driver07)
        gettable(7, driver07)
        getstatistics(7, driver07)


class getpage8(threading.Thread):
    def run(self):
        driver08 = webdriver.Chrome(chrome_options=option)
        driver08.get('https://www.taptap.com/top/ios/played')
        getpage(8, driver08)
        gettable(8, driver08)
        getstatistics(8, driver08)


class getpage9(threading.Thread):
    def run(self):
        driver09 = webdriver.Chrome(chrome_options=option)
        driver09.get('https://www.taptap.com/top/ios/played')
        getpage(9, driver09)
        gettable(9, driver09)
        getstatistics(9, driver09)


class getpage10(threading.Thread):
    def run(self):
        driver10 = webdriver.Chrome(chrome_options=option)
        driver10.get('https://www.taptap.com/top/ios/played')
        getpage(10, driver10)
        gettable(10, driver10)
        getstatistics(10, driver10)


def multi_thread():
    t6 = getpage6()
    t7 = getpage7()
    t8 = getpage8()
    t9 = getpage9()
    t10 = getpage10()

    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()

    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()


if __name__ == '__main__':
    lock.acquire()
    multi_thread()
    lock.release()
    for top, name, firm, score, category, tag, statistics in zip(toplist, namelist, firmlist, scorelist, categorylist, taglist, statisticslist):
        game = {
            "游戏排名": top,
            "游戏名称": name,
            "游戏厂商": firm,
            "游戏评分": score,
            "游戏分类": category,
            "游戏标签": tag,
            "游戏数据": statistics
        }
        games.append(game)
        print(game)

    test = pd.DataFrame(data=games)
    test.to_csv('E:/TapTap/2021.1.6/IOS_HotPlayed.csv', encoding="utf_8_sig", index=False, mode='a+', header=False)

