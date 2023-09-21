from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--ignore-certificate-errors') 


############################################################################
#### THIS BOT IS MEANT TO BE USED TO LOGIN INTO A LEAGUE IN THE         ####
#### ESPN FANTASY FOOTBALL SITE THAT YOU ALREADY ARE IN.                ####
#### SO IN DRIVER.GET() YOU HAVE TO PUT THE EXACT LINK THAT IS USED     ####
#### FOR THE LEAGUE YOU WANT TO TRY THIS BOT ON.                        ####

# Opening ESPN fantasy league
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("REPLACE THIS TEXT WITH THE LINK FOR YOUR LEAGUE")
driver.maximize_window()
time.sleep(3)

# Click on login popup frame
iframe = driver.find_element(By.ID, "oneid-iframe")
driver.switch_to.frame(iframe)
time.sleep(3)

# Log in to espn
username_input = driver.find_element(By.ID, "InputLoginValue")
password_input = driver.find_element(By.ID, "InputPassword")
# Fill in your email here
username_input.send_keys("REPLACE THIS TEXT WITH THE EMAIL USED FOR YOUR ACCOUNT")
# Fill in your password here
password_input.send_keys("REPLACE THIS TEXT WITH THE PASSWORD ATTACHED TO THE ACCOUNT")
password_input.send_keys(Keys.RETURN)
time.sleep(5)
