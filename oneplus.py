import sys
import requests
import os
import time
import telepot
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
#from fake_useragent import UserAgent
import time

from bs4 import BeautifulSoup as soup
from selenium.webdriver.common.keys import Keys
import pymouse
from selenium.webdriver.common.action_chains import ActionChains

while 1:
	try:
		chrome_options = Options()
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--disable-dev-shm-usage')
		chrome_options.add_argument("--start-maximized")
		#chrome_options.add_extension('crx.crx.crx')
		driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chrome_options)
		#driver.set_window_size(1920, 1376)
		driver.get('https://web2.chknet.eu')
		time.sleep(10)
		driver.find_element_by_id('connect:nick').send_keys('vincere')
		driver.find_element_by_id('connect:password').send_keys('shdggfj')
		b = driver.find_elements_by_tag_name('button')
		for bb in b:
			print(bb.text)
			if 'CONNECT' in bb.text.encode('utf-8'):
				print(bb.text)
				bb.click()
				break
		time.sleep(5)
		chrome_options_1 = Options()
		chrome_options_1.add_argument('--headless')
		chrome_options_1.add_argument('--no-sandbox')
		chrome_options_1.add_argument('--disable-dev-shm-usage')
		chrome_options_1.add_argument("--start-maximized")
		#chrome_options.add_extension('crx.crx.crx')
		driver_1 = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chrome_options_1)
		#driver.set_window_size(1920, 1376)
		driver_1.get('https://id.heroku.com/login')
		time.sleep(10)
		driver_1.find_element_by_id('email').send_keys('gangwar.shobhit81@gmail.com')
		driver_1.find_element_by_id('password').send_keys('1@bareilly9997255049')
		driver_1.find_element_by_name('commit').click()
		time.sleep(10)
		driver_1.get('https://dashboard.heroku.com/account/billing')
		time.sleep(10)
		button = driver_1.find_elements_by_tag_name('button')
		for b in button:
			print(b.text)
			if 'Add credit' in b.text.encode("utf-8"):
				b.click()
				break
		time.sleep(10)
		driver_1.save_screenshot('initial1.png')
		driver.save_screenshot('initial.png')
		driver_1.find_element_by_id('firstname').send_keys('Anes')
		driver_1.find_element_by_id('lastname').send_keys('AS')
		driver_1.find_element_by_id('billing-address').send_keys('X-1 ZombieLAnd')
		driver_1.find_element_by_id('address-level2').send_keys('New York')
		sel = driver_1.find_elements_by_tag_name('select')[1]
		#print(len(sel))
		Select(sel).select_by_value('NY')
		driver_1.find_element_by_id('postal').send_keys('10001')
		"""actions = ActionChains(driver_1)
		actions.key_down(Keys.SHIFT)
		actions.send_keys(Keys.TAB)
		actions.send_keys(Keys.TAB)
		actions.send_keys(Keys.TAB)
		actions.send_keys(Keys.TAB)
		actions.send_keys(Keys.TAB)
		actions.send_keys(Keys.TAB)
		actions.send_keys(Keys.TAB)
		actions.send_keys(Keys.TAB)
		actions.send_keys(Keys.TAB)
		actions.send_keys(Keys.TAB)
		actions.send_keys(Keys.TAB)
		actions.send_keys(Keys.TAB)
		actions.key_up(Keys.SHIFT)
		actions.perform()"""
		#time.sleep(100)
		ch = driver.find_elements_by_tag_name('span')
		for c in ch:
			print(c.text)
			if '#unix' in c.text:
				c.click()
				break
		previous_count = 0
		flag = 1
		while 1:
			#if flag == 1:
			#	exit()
			try:
				error = driver.find_element_by_id('user-visible-error')
				print(error.text.encode('utf-8'))
				if 'DISCONNECTED' in error.text.encode('utf-8'):
					error.click()
			except Exception as e:
				pass
			data = driver.find_elements_by_class_name('content') 
			for d in data[previous_count:len(data)]:
				flag = 1
				print(d.text)
				if '!chk' in d.text or '!CHK' in d.text:
					card_info = d.text[5:]
					if '|' in card_info:
						card_num = card_info.split('|')
						size = len(card_num)
						if card_num[size-1][0].isalpha():
							size = size-1
						card_number = card_num[0]
						if len(card_num[1])<3:
							card_date = (card_num[1])+str(card_num[2])
							card_cvv = (card_num[3])
						else:
							card_date = (card_num[1])
							card_cvv = (card_num[2])				
						driver_1.switch_to.frame(driver_1.find_element_by_id('braintree-hosted-field-number'))
						driver_1.find_element_by_name('credit-card-number').send_keys(Keys.CONTROL,'a')
						driver_1.find_element_by_name('credit-card-number').send_keys(card_num)
						driver_1.switch_to.default_content()
						driver_1.switch_to.frame(driver_1.find_element_by_id('braintree-hosted-field-expirationDate'))
						driver_1.find_element_by_name('expiration').send_keys(Keys.CONTROL,'a')
						driver_1.find_element_by_name('expiration').send_keys(card_date)
						driver_1.switch_to.default_content()
						driver_1.switch_to.frame(driver_1.find_element_by_id('braintree-hosted-field-cvv'))
						driver_1.find_element_by_name('cvv').send_keys(Keys.CONTROL,'a')
						driver_1.find_element_by_name('cvv').send_keys(card_cvv)
						driver_1.switch_to.default_content()
						driver_1.find_elements_by_tag_name('button')[2].click()
						time.sleep(5)
						driver_1.save_screenshot('initial.png')
						span = driver_1.find_elements_by_tag_name('span')
						i = 0
						for s in span:
							print(s.text+'  ........... '+str(i))
							i = i+1
							#if 'Error' in s.text.encode('utf-8'):
							#	continue
					if card_info[16] == ' ':
						if card_info[19] == ' ':
							card_num = card_info[:16]
							card_date = card_info[17:21]
							card_date = card_date.strip(" ")
							card_cvv =  card_info[23:25]
							print(card_num)
							print(card_date)
							print(card_cvv)
							driver_1.switch_to.frame(driver_1.find_element_by_id('braintree-hosted-field-number'))
							driver_1.find_element_by_name('credit-card-number').send_keys(Keys.CONTROL,'a')
							driver_1.find_element_by_name('credit-card-number').send_keys(card_num)
							driver_1.switch_to.default_content()
							driver_1.switch_to.frame(driver_1.find_element_by_id('braintree-hosted-field-expirationDate'))
							driver_1.find_element_by_name('expiration').send_keys(Keys.CONTROL,'a')
							driver_1.find_element_by_name('expiration').send_keys(card_date)
							driver_1.switch_to.default_content()
							driver_1.switch_to.frame(driver_1.find_element_by_id('braintree-hosted-field-cvv'))
							driver_1.find_element_by_name('cvv').send_keys(Keys.CONTROL,'a')
							driver_1.find_element_by_name('cvv').send_keys(card_cvv)
							driver_1.switch_to.default_content()
							driver_1.find_elements_by_tag_name('button')[2].click()
							time.sleep(5)
							driver_1.save_screenshot('initial.png')
							span = driver_1.find_elements_by_tag_name('span')
							i = 0
							for s in span:
								print(s.text+'  ........... '+str(i))
								i = i+1
								#if 'Error' in s.text.encode('utf-8'):
								#	continue
						if card_info[19] != ' ':
							card_num = card_info[:16]
							card_date = card_info[17:21]
							#card_date = card_date.strip(" ")
							card_cvv =  card_info[22:25]
							print(card_num)
							print(card_date)
							print(card_cvv)
							driver_1.switch_to.frame(driver_1.find_element_by_id('braintree-hosted-field-number'))
							driver_1.find_element_by_name('credit-card-number').send_keys(Keys.CONTROL,'a')
							driver_1.find_element_by_name('credit-card-number').send_keys(card_num)
							driver_1.switch_to.default_content()
							driver_1.switch_to.frame(driver_1.find_element_by_id('braintree-hosted-field-expirationDate'))
							driver_1.find_element_by_name('expiration').send_keys(Keys.CONTROL,'a')
							driver_1.find_element_by_name('expiration').send_keys(card_date)
							driver_1.switch_to.default_content()
							driver_1.switch_to.frame(driver_1.find_element_by_id('braintree-hosted-field-cvv'))
							driver_1.find_element_by_name('cvv').send_keys(Keys.CONTROL,'a')
							driver_1.find_element_by_name('cvv').send_keys(card_cvv)
							driver_1.switch_to.default_content()
							driver_1.find_elements_by_tag_name('button')[2].click()
							time.sleep(5)
							driver_1.save_screenshot('initial.png')
							span = driver_1.find_elements_by_tag_name('span')
							i = 0
							for s in span:
								print(s.text+'  ........... '+str(i))
								i = i+1
								#if 'Error' in s.text.encode('utf-8'):
								#	continue
						if card_info[19] == '/':
							card_num = card_info[:16]
							card_date = card_info[17:21]
							card_date = card_date.strip("/")
							card_cvv =  card_info[23:25]
							print(card_num)
							print(card_date)
							print(card_cvv)
							driver_1.switch_to.frame(driver_1.find_element_by_id('braintree-hosted-field-number'))
							driver_1.find_element_by_name('credit-card-number').send_keys(Keys.CONTROL,'a')
							driver_1.find_element_by_name('credit-card-number').send_keys(card_num)
							driver_1.switch_to.default_content()
							driver_1.switch_to.frame(driver_1.find_element_by_id('braintree-hosted-field-expirationDate'))
							driver_1.find_element_by_name('expiration').send_keys(Keys.CONTROL,'a')
							driver_1.find_element_by_name('expiration').send_keys(card_date)
							driver_1.switch_to.default_content()
							driver_1.switch_to.frame(driver_1.find_element_by_id('braintree-hosted-field-cvv'))
							driver_1.find_element_by_name('cvv').send_keys(Keys.CONTROL,'a')
							driver_1.find_element_by_name('cvv').send_keys(card_cvv)
							driver_1.switch_to.default_content()
							driver_1.find_elements_by_tag_name('button')[2].click()
							time.sleep(5)
							driver_1.save_screenshot('initial.png')
							span = driver_1.find_elements_by_tag_name('span')
							i = 0
							for s in span:
								print(s.text+'  ........... '+str(i))
								i = i+1
								#if 'Error' in s.text.encode('utf-8'):
								#	continue
			previous_count = len(data)
	except Exception as e:
		print(e)