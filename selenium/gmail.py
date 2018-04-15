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

driver.get("https://gmail.com/")
wait = WebDriverWait(driver, 600)

x_arg = "//div[text()='COMPOSE']"

group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
print(group_title)
group_title.click()
print("clicked")

to_xpath = "//textarea[@name='to']"
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, to_xpath)))
to_email = "kalpesh.bansal.eee15@iitbhu.ac.in"
input_box.send_keys(to_email + Keys.ENTER)
time.sleep(1)

subj_xpath = "//input[@name='subjectbox']"
subject = "mail through python :D"
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, subj_xpath)))
input_box.send_keys(subject + Keys.ENTER)
time.sleep(1)

msg_body = "Bro! \n Aja room par script is done :D\n\n\n Sent through python"
msg_xpath = "//div[@aria-label='Message Body']"
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, msg_xpath)))
input_box.send_keys(msg_body + Keys.ENTER)
time.sleep(1)

file_input = driver.execute_script(
 "var input = document.createElement('input');"
 "input.type = 'file';"
 "input.style.display = 'block';"
 "if (document.body.childElementCount > 0) {"
 " document.body.insertBefore("
 " input, document.body.childNodes[0]"
 " );"
 "} else {"
 " document.body.appendChild(input);"
 "}"
 "return input;"
)
def dispatch_file_drag_event(event_name, to, file_input_element):
 	driver.execute_script(
	 "var event = document.createEvent('CustomEvent');"
	 "event.initCustomEvent(arguments[0], true, true 0);"
	 "event.dataTransfer = {"
	 " files: arguments[1].files"
	 "};"
	 "arguments[2].dispatchEvent(event);",
	 event_name, file_input_element, to)
 	
file_input.send_keys('/home/ags/test.txt')
dispatch_file_drag_event('dragenter', 'document', file_input)
drag_target = driver.find_element_by_xpath(
 "//div[text()='Drop files here']"
)
dispatch_file_drag_event('drop', drag_target, file_input)
driver.execute_script(
 "arguments[0].parentNode.removeChild(arguments[0]);", file_input
)


send_xpath = "//div[text()='Send']"
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, send_xpath)))
input_box.send_keys(Keys.ENTER)

time.sleep(1)
