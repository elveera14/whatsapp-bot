#selenium for all web operations.
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time

# BeautifulSoup to scrap data from a website.
from bs4 import BeautifulSoup
from requests import get


def scrapdata():
    #we'll scrap data from this url.
    url = 'https://www.91mobiles.com/phonefinder.php'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    #we'll get name and price of top 10 mobiles.
    names = []
    prices = []
    
    #finally start scrapping..
    containers = html_soup.find_all('div', class_ = 'filter filer_finder')

    for container in containers:
        name = container.h3.a.text
        names.append(name)
        price = container.find('span', class_ = 'price price_padding').text
        prices.append(price)
        input_box.send_keys(name + price + Keys.ENTER)

#location of driver
driver = webdriver.Chrome('/home/odoo/Hetal/chromedriver') 

#open whasapweb
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 
  
#name of the contact
target = '"Elveera"'

#search for given contact name
x_arg = '//span[contains(@title,' + target + ')]'

#wait until it's available
group_title = wait.until(EC.presence_of_element_located(( 
    By.XPATH, x_arg))) 

#click on it to open the chat
group_title.click()
inp_xpath = '//div[@dir="ltr"][@data-tab="1"][@spellcheck="true"]'

#input box to type stuff
input_box = wait.until(EC.presence_of_element_located(( 
    By.XPATH, inp_xpath)))

#send initial message
input_box.send_keys("Please Enter a commad.." + Keys.ENTER)

#just ensuring we save this element once the message has been sent
time.sleep(1)
message = driver.find_elements_by_class_name("FTBzM")[-1]

#wait for 10 seconds for the reply and save it in a new variable
time.sleep(10)
new_message = driver.find_elements_by_class_name("FTBzM")[-1]

#now just see if there is a reply....
if message != new_message:
    if "mobiles" in new_message.text:
        scrapdata()
    else:
        input_box.send_keys("Wrong command. Please enter a valid command!!!" + Keys.ENTER)
else:
    input_box.send_keys("Timed out!!" + Keys.ENTER)
