from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
from win10toast import ToastNotifier
import json
import re

options = Options()
options.add_experimental_option("detach", True)
svc = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc, options=options)
actions = ActionChains(driver)

Toaster = ToastNotifier()
Toaster.show_toast("Typewriter-BOT", "Typewriter has been started", duration=2)

speed = 0
error_rate_percent = 0.00001

def random_chance(percentage):
    return random.random() <= percentage


def Lektion():
    Lektion = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[1]")
    lektion = Lektion.text
    number_match = re.search(r'Lektion\s*:\s*(\d+)', lektion)
    if number_match:
        lesson_number = number_match.group(1)
        return lesson_number

def new_level():
    global speed
    global error_rate_percent	
    lektion = Lektion()
    print(f"Extracted lesson number: {lektion}")
    level_string = f"Level {lektion}"
    print(f"Level string: {level_string}")
    with open('level_data.json', 'r') as json_file:
        level_data = json.load(json_file)
    if level_string in level_data:
        speed = level_data[level_string]['Speed']
        error_rate_percent = level_data[level_string]['Error Rate']
        print(f"Updated speed and error rate for lesson {lektion}")
    else:
        level_data[level_string] = {'Speed': speed, 'Error Rate': error_rate_percent}
        print(f"Added new lesson {lektion} with speed and error rate")
    speed += 200
    speed = speed / 10 
    speed = 60 / speed
    


driver.get('https://at4.typewriter.at/')
time.sleep(0.75) 
driver.find_element("xpath","/html/body/div[6]/div[2]/div[1]/div[2]/div[2]/button[1]/p").click()

with open('logindata.json', 'r') as json_file:
    login_data = json.load(json_file)

driver.find_element("xpath",'/html/body/div[4]/div[2]/div[1]/form/div[1]/input').send_keys(login_data["username"])
driver.find_element("xpath",'/html/body/div[4]/div[2]/div[1]/form/div[2]/input').send_keys(login_data["password"])
driver.find_element("xpath",'/html/body/div[4]/div[2]/div[1]/form/div[3]/input').click()
time.sleep(2)
runlevelB = driver.find_element("xpath",'//*[@id="contentBody"]/div[1]/div[1]/a')
runlevelB.click()
time.sleep(1)

new_level()

print(f"Speed: {speed}")
print(f"Error Rate: {error_rate_percent}")

count = 0
count2 = 0
while True:
    try:
        if random_chance(error_rate_percent):
            actions.send_keys("a").perform()
        element = driver.find_element(By.XPATH, "//div[@id='text_todo_1']/span[1]")
        wert_des_elements = element.text
        actions.send_keys(wert_des_elements).perform()
        time.sleep(speed)
    except:
        count2 += 1
        print("trying...")
        if count2 > 30:
            driver.find_element("xpath","/html/body/div[5]/div[1]/div[2]/ul/li[3]/a/div").click()
            #newbeginning
            time.sleep(1)
            count = 0
            count2 = 0

            print("New Lesson")
            new_level()
