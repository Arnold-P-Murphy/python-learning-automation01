
'''
This module demonstrates how to automate a basic browser
task using Selenium. This example automates the process
of filling out a registration form on an e-commerce website.
It includes importing necessary libraries, setting up the
Chrome WebDriver, and filling out the form fields.

Author: Arnold Murphy
Date: 2025-04-29
'''

# import relevant libraries
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# define url
URL = (
  "https://ecommerce-playground.lambdatest.io/"
  "index.php?route=account/register"
)

# instantiate webdriver and open a chrome browser
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# maximize browser window
driver.maximize_window()

# load the webpage
driver.get(URL)

# find the first name field
first_name = driver.find_element(By.XPATH, '//*[@id="input-firstname"]')
# fill out the first name field
first_name.send_keys("Johnny")

# find the last name field
last_name = driver.find_element(By.XPATH, '//*[@id="input-lastname"]')
# find the last name field
last_name.send_keys("Smith")

# find the email field
email = driver.find_element(By.XPATH, '//*[@id="input-email"]')
# fill in the email field
email.send_keys("john.smith@team201666.testinator.com")

# find the telephone field
telephone = driver.find_element(By.XPATH, '//*[@id="input-telephone"]')
# fill in the telephone field
telephone.send_keys("306-764-1234")

# find the password field
password = driver.find_element(By.XPATH, '//*[@id="input-password"]')
# fill in the password field
password.send_keys("|74NpsXN3'0d")

# find the password confirm field
password_confirm = driver.find_element(By.XPATH, '//*[@id="input-confirm"]')
# fill in the password confirm field
password_confirm.send_keys("|74NpsXN3'0d")

# find the desired response to the newsletter subscribe field
newsletter_subscribe = driver.find_element(
    By.XPATH,
    (
        '/html/body/div[1]/div[5]/div[1]/div/div/form/fieldset[3]/div/div/'
        'div[2]/label'
    )
)
# click on it
newsletter_subscribe.click()

# find the checkbox for agreeing to the terms
agree = driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[5]/div[1]/div/div/form/div/div/div/label'
)
# click on the agree checkbox
agree.click()

# find the continue button
continue_button = driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[5]/div[1]/div/div/form/div/div/input'
)
# click on the continue button
continue_button.click()

# scroll down by 200 units to view the lower part of the page
driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

# pause the program for 5 seconds to view the results
sleep(5)

# close the driver
driver.quit()


# End-of-file (EOF)
