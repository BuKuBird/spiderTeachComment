import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
# 创建浏览器操作对象
browser = webdriver.Chrome(options=option)

stuNum = "" # 教务网账号
passNum = "" # 教务网密码
# 访问网站
url = 'http://jwxt.fjjxu.edu.cn:81/jwglxt/xtgl/login_slogin.html'
url2 = 'http://jwxt.fjjxu.edu.cn:81/jwglxt/xspjgl/xspj_cxXspjIndex.html?doType=details&gnmkdm=N401605&layout=default'

browser.get(url)
browser.maximize_window()

time.sleep(0.5)
uname = browser.find_element(By.XPATH,'//*[@id="yhm"]')
uname.send_keys(f"{stuNum}")

time.sleep(0.2)

upass = browser.find_element(By.XPATH,'//*[@id="mm"]')
upass.send_keys(f"{passNum}")

time.sleep(0.2)

submit = browser.find_element(By.XPATH,'//*[@id="dl"]').click()

time.sleep(1)
browser.get(url2)
time.sleep(1)
time1 = browser.find_element(By.XPATH,'//*[@id="wp"]/span').text
time2 = browser.find_element(By.XPATH,'//*[@id="bc"]/span').text
time3 = browser.find_element(By.XPATH,'//*[@id="tj"]/span').text
for tr in range(int(time1)+int(time2)+int(time3)):
    browser.find_element(By.XPATH,f'//*[@id="tempGrid"]/tbody/tr[@id = "{tr+1}"]/td[9]').click()
    time.sleep(1)
    for i in range(5):
        time.sleep(0.2)
        for td in range(4):
            items = browser.find_element(By.XPATH,f'//*[@id="ajaxForm1"]/div[2]/div[1]/div[2]/table[{i+1}]/tbody/tr[{td+1}]/td[2]/div/input').send_keys("100")
            time.sleep(0.2)
    comment = browser.find_element(By.XPATH,'//*/textarea').send_keys("100")
    time.sleep(0.2)
    save = browser.find_element(By.XPATH, '//*[@id="btn_xspj_bc"]').click()
    time.sleep(0.25)
    ok = browser.find_element(By.XPATH,'//*[@id="btn_ok"]').click()

# xueshengpingjia = browser.find_element(By.XPATH,'//*[@id="cdNav"]/ul/li[5]/ul/li[1]/a').click()