import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})


driver = webdriver.Chrome(chrome_options=option, executable_path='C:\chromedriver')
driver.get("http://wolf.bet")
driver.find_element_by_name('header-login').click()
driver.find_element_by_name('Username / Email').send_keys('lnsomnia')
driver.find_element_by_name('Password').send_keys('1995tiger')
driver.find_element_by_name('login-submit').click()
driver.implicitly_wait(3)
balance = float(driver.find_element_by_class_name('balance__currency--value-big').text.strip())

bet_amount_input = driver.find_element_by_name('bet_amount')
bet_amount_val = 0.01
ROLL_BUTTON = driver.find_element_by_css_selector('.game-controller__button-main')

def roll_dice():

    balance = float(driver.find_element_by_class_name('balance__currency--value-big').text.strip())
    # bet_amount_val = float(driver.find_element_by_name('bet_amount').get_attribute('value').strip())
    logging.info('BALANCE IS: ', balance)
    logging.info('CURRENT BET IS: ', bet_amount_val)
    while balance <= 5.0:
        logging.info('Starting low balance loop...')
        bet_amount_input.clear()
        bet_amount_input.send_keys(str(bet_amount_val))
        driver.implicitly_wait(1)
        ROLL_BUTTON.click()
        check_for_win()

def check_for_win():
    last_bet = driver.find_element_by_css_selector('.last-bets__element.positive').value_of_css_property(
        'background-color').strip()
    if last_bet == 'rgba(7, 214, 7, 1)':
        logging.info('Success! Rolling again...')
        roll_dice()
    logging.info('Fail! Doubling bet and rolling again...')
    double_bet()
    roll_dice()


def double_bet():
    bet_amount_input.send_keys(str(bet_amount_val * 2))


roll_dice()



# driver.find_element_by_id('MemberPassword2').send_keys('Cxzcxz4*')
# driver.find_element_by_name('captchaSubmit').click()
# driver.implicitly_wait(1000)
# driver.find_element_by_link_text('Earn $0.25').click()
# current_survery = driver.current_url
# driver.get(current_survery)
# driver.implicitly_wait(500)
# driver.find_elements_by_link_text('Play').click()