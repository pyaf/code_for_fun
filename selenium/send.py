from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
# Replace below path with the absolute path
# to chromedriver in your computer
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

driver = webdriver.Chrome(os.path.join(BASE_DIR, 'chromedriver'))
#open tab
# driver = webdriver.Firefox()
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# your friend's name in your contact list
target = '"BHU Mantri"'

# Replace the below string with your own message
string = "lol"

x_arg = '//span[contains(@title,' + target + ')]'
print(x_arg)
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
print(group_title)
group_title.click()
print("clicked")
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
print(inp_xpath)
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
print(input_box)
for i in range(100):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)
