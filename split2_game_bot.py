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
    time.sleep(5)
    driver.find_elements_by_xpath("//*[contains(text(), 'SwapIt 2')]")
    driver.find_element_by_xpath('//*[@id="gameList_2"]/ul/li[1]/span[1]/a').click()
    driver.find_element_by_name('PlayButton151520_0').click()


def play_game():
    # TODO: Get version number to check for game updates
    time.sleep(4)
    driver.find_element_by_class_name('start_txt').click()
    driver.find_element_by_id('confirm_txt').click()
    # TODO: Set anti-ban behavior to sleep at random intervals at random time
    time.sleep(6)
    x01 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[57]/div').value_of_css_property('background-image')
    x02 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[58]/div').value_of_css_property('background-image')
    x03 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[59]/div').value_of_css_property('background-image')
    x04 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[60]/div').value_of_css_property('background-image')
    x05 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[61]/div').value_of_css_property('background-image')
    x06 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[62]/div').value_of_css_property('background-image')
    x07 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[63]/div').value_of_css_property('background-image')
    x08 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[64]/div').value_of_css_property('background-image')
    x09 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[49]/div').value_of_css_property('background-image')
    x10 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[50]/div').value_of_css_property('background-image')
    x11 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[51]/div').value_of_css_property('background-image')
    x12 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[52]/div').value_of_css_property('background-image')
    x13 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[53]/div').value_of_css_property('background-image')
    x14 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[54]/div').value_of_css_property('background-image')
    x15 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[55]/div').value_of_css_property('background-image')
    x16 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[56]/div').value_of_css_property('background-image')
    x17 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[41]/div').value_of_css_property('background-image')
    x18 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[42]/div').value_of_css_property('background-image')
    x19 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[43]/div').value_of_css_property('background-image')
    x20 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[44]/div').value_of_css_property('background-image')
    x21 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[45]/div').value_of_css_property('background-image')
    x22 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[46]/div').value_of_css_property('background-image')
    x23 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[47]/div').value_of_css_property('background-image')
    x24 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[48]/div').value_of_css_property('background-image')
    x25 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[33]/div').value_of_css_property('background-image')
    x26 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[34]/div').value_of_css_property('background-image')
    x27 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[35]/div').value_of_css_property('background-image')
    x28 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[36]/div').value_of_css_property('background-image')
    x29 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[37]/div').value_of_css_property('background-image')
    x30 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[38]/div').value_of_css_property('background-image')
    x31 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[39]/div').value_of_css_property('background-image')
    x32 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[40]/div').value_of_css_property('background-image')
    x33 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[25]/div').value_of_css_property('background-image')
    x34 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[26]/div').value_of_css_property('background-image')
    x35 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[27]/div').value_of_css_property('background-image')
    x36 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[28]/div').value_of_css_property('background-image')
    x37 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[29]/div').value_of_css_property('background-image')
    x38 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[30]/div').value_of_css_property('background-image')
    x39 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[31]/div').value_of_css_property('background-image')
    x40 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[32]/div').value_of_css_property('background-image')
    x41 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[17]/div').value_of_css_property('background-image')
    x42 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[18]/div').value_of_css_property('background-image')
    x43 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[19]/div').value_of_css_property('background-image')
    x44 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[20]/div').value_of_css_property('background-image')
    x45 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[21]/div').value_of_css_property('background-image')
    x46 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[22]/div').value_of_css_property('background-image')
    x47 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[23]/div').value_of_css_property('background-image')
    x48 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[24]/div').value_of_css_property('background-image')
    x49 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[9]/div').value_of_css_property('background-image')
    x50 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[10]/div').value_of_css_property('background-image')
    x51 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[11]/div').value_of_css_property('background-image')
    x52 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[12]/div').value_of_css_property('background-image')
    x53 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[13]/div').value_of_css_property('background-image')
    x54 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[14]/div').value_of_css_property('background-image')
    x55 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[15]/div').value_of_css_property('background-image')
    x56 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[16]/div').value_of_css_property('background-image')
    x57 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[9]/div').value_of_css_property('background-image')
    x58 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[1]/div').value_of_css_property('background-image')
    x59 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[2]/div').value_of_css_property('background-image')
    x60 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[3]/div').value_of_css_property('background-image')
    x61 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[4]/div').value_of_css_property('background-image')
    x62 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[5]/div').value_of_css_property('background-image')
    x63 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[6]/div').value_of_css_property('background-image')
    x64 = driver.find_element_by_xpath('//*[@id="cell-board"]/div[7]/div').value_of_css_property('background-image')

    board = [
        [x01, x02, x03, x04, x05, x06, x07, x08],
        [x09, x10, x11, x12, x13, x14, x15, x16],
        [x17, x18, x19, x20, x21, x22, x23, x24],
        [x25, x26, x27, x28, x29, x30, x31, x32],
        [x33, x34, x35, x36, x37, x38, x39, x40],
        [x41, x42, x43, x44, x45, x46, x47, x48],
        [x49, x50, x51, x52, x53, x54, x55, x56],
        [x57, x58, x59, x60, x61, x62, x63, x64]
    ]

    # TODO: write out logic for drag and drop using selenium

    for i in board:
        for j in i:
            print(("Piece {}: " + j).format(i), end=" ")
        # TODO: Print colored symbol to represent each colored piece on the board
        print()
    driver.find_element_by_xpath('//*[@id="cell-board"]/div[57]/div')

    # TODO: run loop to play game on loop after each piece move


def start_bot():
    login_to_site()
    navigate_to_game()
    play_game()

start_bot()