from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')

name = input('Enter name of contact or group: ')
input('Enter anything after scaning QR code: ')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click

msg = input('Enter message: ')
while msg != 'stop!':
    msgBox = driver.find_element_by_xpath('//div[@class = "_2S1VP"] | //div[@data-tab="1"]')
    msgBox.send_keys(msg)
    driver.find_element_by_class_name('_35EW6').click()
    msg = input('Enter message: ')