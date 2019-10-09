import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome('C:\chromedriver')

def login_to_site():
    driver.get("https://www.worldwinner.com/")
    time.sleep(7)
    driver.find_element_by_css_selector(
        '.JoinNowHeaderWrapper .JoinNowHeaderPanel .mainNavBar a.ww_button:active, .JoinNowHeaderWrapper .JoinNowHeaderPanel .mainNavBar a.ww_button:hover, .JoinNowHeaderWrapper .JoinNowHeaderPanel .mainNavBar a.ww_button:link, .JoinNowHeaderWrapper .JoinNowHeaderPanel .mainNavBar a.ww_button:visited').click()
    driver.find_element_by_name('username').send_keys('brandon_n_evans@live.com')
    driver.find_element_by_name('password').send_keys('Cxzcxz4*')
    driver.find_element_by_css_selector(
        '.ModalContent .HomepageAuthentication .login .buttons .ww_button, .ModalContent .HomepageAuthentication .registration .buttons .ww_button').click()

def navigate_to_game():
    time.sleep(3)
    driver.find_elements_by_xpath("//*[contains(text(), 'SwapIt 2')]")
    driver.find_element_by_xpath('//*[@id="gameList_2"]/ul/li[1]/span[1]/a').click()
    driver.find_element_by_name('PlayButton151520_0').click()


def start_bot():
    login_to_site()
    navigate_to_game()

start_bot()