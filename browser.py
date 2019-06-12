from selenium import webdriver
browser = webdriver.Chrome("chromedriver")
browser.get('https://www.seleniumhq.org')
elem = browser.find_element_by_link_text('Download')
elem.text