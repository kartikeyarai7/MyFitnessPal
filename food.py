from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.myfitnesspal.com/account/login')  #Searching Myfitness Pal
driver.maximize_window()

email = driver.find_element_by_xpath('//*[@id="username"]')
email.send_keys("Kartikeyarai7@gmail.com")
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("Bareilly7")  

time.sleep(3)

login = driver.find_element_by_xpath('//*[@id="content"]/form/div/ul/li[5]/input')
login.click()   #Logging In

time.sleep(10)

# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'r')

close = driver.find_element_by_xpath('//*[@id="ember1926"]/div[2]/div[1]/div[2]/a')  #Closing the popup
close.click()

time.sleep(5)

add_food = driver.find_element_by_xpath('//*[@id="ember1718"]') #Adding food 
add_food.click()

time.sleep(5)

# search = driver.find_element_by_xpath('//*[@id="search"]')
# search.send_keys("Milk")

breakfast_add_food = driver.find_element_by_xpath('//*[@id="diary-table"]/tbody/tr[2]/td[1]/a')
breakfast_add_food.click()

time.sleep(5)

milk = driver.find_element_by_xpath('//*[@id="favorites_51_checked"]')
corn_flakes = driver.find_element_by_xpath('//*[@id="favorites_50_checked"]')
threptin = driver.find_element_by_xpath('//*[@id="favorites_55_checked"]')
banana = driver.find_element_by_xpath('//*[@id="favorites_57_checked"]')
add_btn = driver.find_element_by_xpath('//*[@id="add_button_en"]')
breakfast_items = [milk, corn_flakes, threptin, banana]

for item in breakfast_items:  #Breakfast
    item.click()
 
add_btn.click()   #Breakfast items added

time.sleep(5)

lunch_add_food = driver.find_element_by_xpath('//*[@id="diary-table"]/tbody/tr[8]/td[1]/a')  #Lunch
lunch_add_food.click()


time.sleep(5)

roti = driver.find_element_by_xpath('//*[@id="favorites_53_checked"]')
dal = driver.find_element_by_xpath('//*[@id="favorites_52_checked"]')
rice = driver.find_element_by_xpath('//*[@id="favorites_50_checked"]')
add_btn2 = driver.find_element_by_xpath('//*[@id="add_button_en"]')
# paneer = driver.find_element_by_xpath('//*[@id="favorites_57_checked"]')
lunch_items = [roti,dal,rice]

for item in lunch_items:
    item.click() 

add_btn2.click() #Lunch items added

time.sleep(5)

post_workout_add = driver.find_element_by_xpath('//*[@id="diary-table"]/tbody/tr[17]/td[1]/a')
post_workout_add.click()

time.sleep(5)

nitro_tech = driver.find_element_by_xpath('//*[@id="favorites_7_checked"]')
nitro_tech.click()
add_btn.click() #Post workout items added

time.sleep(5)

done = driver.find_element_by_xpath('//*[@id="complete_day"]/span/a')
done.click()

time.sleep(5)

log_out = driver.find_element_by_xpath('//*[@id="navTop"]/li[5]/a')  #Log out
time.sleep(5)
driver.close() #Close