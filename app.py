from selenium import webdriver
import requests
import os
import time
from bs4 import BeautifulSoup

# root_dir = 'douban/image'
# if not os.path.exists(root_dir):
#     os.mkdir(root_dir)

# 浏览器
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values': {
        'images': 2,
        #'javascript': 2
    }
}
options.add_experimental_option('prefs', prefs)


driver = webdriver.Chrome(executable_path="./chromedriver",chrome_options=options)
driver.set_script_timeout(3)
driver.get("https://accounts.douban.com/passport/login")

time.sleep(3)

driver.find_element_by_class_name("account-tab-account").click()

driver.find_element_by_css_selector("#username").send_keys("18502833582")

driver.find_element_by_css_selector("#password").send_keys("wule3695210")

driver.find_elements_by_css_selector(".account-tabcon-start .account-form-field-submit a")

def spider(page):
    base_url = 'https://book.douban.com/tag/小说?type=T&start=%s' % (page * 20)

    # 访问
    driver.get(base_url)

    # file_name = root_dir + '/%s.png'%(page)
    # driver.save_screenshot(file_name)

    # 页面内容
    #print(driver.page_source)

    # 解析
    content_parser(driver.page_source)
    time.sleep(2)


# 解析
def content_parser(content):
    soup = BeautifulSoup(content,'html.parser', from_encoding='utf-8' )

    links = soup.find_all('a')
    for link in links:
        if link.get_text().strip():
            print( link['href'], link.get_text())




if __name__ == '__main__':
    for i in range(11):
        spider(i)
