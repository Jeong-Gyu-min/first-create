import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url) # url로 이동

# 가는 날 선택 click
elem = browser.find_element_by_xpath("//*[@id=\"__next\"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]")
time.sleep(1)
elem.click()

# 이번달 27일, 28일 선택
# time.sleep(2)
# browser.find_element_by_xpath("//*[@id=\"__next\"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/button/b").click()
# time.sleep(2)
# browser.find_element_by_xpath("//*[@id=\"__next\"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[3]/button/b").click()

# 다음달 27일, 28일 선택
time.sleep(2)
browser.find_element_by_xpath("//*[@id=\"__next\"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[5]/td[5]/button/b").click()
time.sleep(2)
browser.find_element_by_xpath("//*[@id=\"__next\"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[5]/td[6]/button").click()

# time.sleep(2)
# browser.find_element_by_link_text("28")[0].click() # 현재 막혀서 안됨(class_name, link_text는 a 클래스가 아니면 참조가 안됨)

browser.find_element_by_xpath("//*[@id=\"__next\"]/div/div[1]/div[6]/div/div[2]/div/ul/li[1]/button/figure/img").click()

time.sleep(2)
browser.find_element_by_class_name("recommend_anchor__1qmYP").click()

# 정상 작동
time.sleep(20)
elem = browser.find_element_by_xpath("//*[@id=\"__next\"]/div/div[1]/div[4]/div/div[3]/div[1]")
print(elem.text)

# 비정상 작동
# try:
#     elem = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"__next\"]/div/div[1]/div[4]/div/div[3]/div[1]"))) # 현재 페이지는 중간에 넘어가서 처음걸 보여줌
#     print(elem.text)
# finally:








