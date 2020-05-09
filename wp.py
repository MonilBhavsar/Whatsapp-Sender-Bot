from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
driver.get('https://web.whatsapp.com')

phonelist = []
for phone in phonelist:

	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'T') 
	driver.get('http://stackoverflow.com/')
	driver.get('https://web.whatsapp.com/send?phone='+phone)


	# user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	# user.click()
	delay = 60 # seconds
	try:
		msg_box = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')))
		msg_box.send_keys("Hello")
		msg_box.send_keys(Keys.ENTER)
		print("Page is ready!")
		sleep(2)
	except TimeoutException:
		print("Loading took too much time!")


