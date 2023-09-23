from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from random import *
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# Créez une boucle pour exécuter le script 100 fois
for _ in range(15):
    website = "https://vote.le-classement.fr/concours/2023/participations/100"

    options = webdriver.ChromeOptions()
    service = Service()
    options.add_argument("user-agent=Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166")
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)

    time.sleep(1)

    driver.get("https://10minutemail.com/session/address")

    pre_element = driver.find_element(By.XPATH, '//pre')
    text = pre_element.text
    data = json.loads(text)
    address = data.get('address', '')

    time.sleep(2)

    print("Adresse:", address)

    driver.get(website)

    time.sleep(2)

    nbr_votes = driver.find_element(
        By.XPATH, "//*[contains(text(),'voix et bientôt la tienne')]")
    vote_text = nbr_votes.text

    votes = vote_text.split(' ')[0]
    print(votes, "votes")

    xpath_expression = '/html/body/main/section[1]/div/header/div[2]/div[2]/div/button'
    button_element = driver.find_element(By.XPATH, xpath_expression).click()

    time.sleep(2)

    email_input = driver.find_element(by=By.NAME, value='email')
    email_input.send_keys(address)

    time.sleep(random())

    click_tick_box1 = driver.find_element(
        By.XPATH, '/html/body/main/section[1]/div/header/div[2]/div[2]/div/div[2]/div[2]/div/form/div[1]/input').click()
    time.sleep(random())
    click_tick_box2 = driver.find_element(
        By.XPATH, '/html/body/main/section[1]/div/header/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/input').click()

    time.sleep(random())

    validate_vote = driver.find_element(
        By.XPATH, '/html/body/main/section[1]/div/header/div[2]/div[2]/div/div[2]/div[2]/div/form/div[3]/button').click()

    time.sleep(1.5)

    driver.get("https://10minutemail.com/")

    time.sleep(25)

    get_url = driver.find_element(
        By.XPATH, "//*[contains(text(),'Confirmer ma voix')]")

    time.sleep(5)

    driver.get(get_url.get_attribute("href"))
    print("vote+1")

    driver.quit()
