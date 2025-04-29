"""
This module demonstrates how to:
Parse text files as data with comma separated values.
line into a list of words.

Author: Arnold Murphy
Date: 2025-04-29
"""

# import relevant libraries
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

# define URL
URL = "https://the-internet.herokuapp.com/dynamic_controls"  # Example:
# "https://the-internet.herokuapp.com/dynamic_controls"

# instantiate Firefox webdriver
gecko_driver_path = GeckoDriverManager().install()
service = FirefoxService(gecko_driver_path)
driver = webdriver.Firefox(service=service)

# maximize browser window
driver.maximize_window()

# load the webpage
driver.get(URL)

# define a wait
wait = WebDriverWait(driver, 10)

# find the Enable button
enable_button = driver.find_element(
  By.XPATH,
  (
    (
        (
            '/html/body/div[2]/div/div[1]/form[2]/button'
            # Example: "//button[text()='Enable']"
        )
    )
  )
)
# click the Enable button
enable_button.click()
sleep(3)

# find the Disable button
# uncomment and replace XPATH
# disable_button = wait.until(
#     EC.element_to_be_clickable((By.XPATH, 'FILL IN'))
# )
# disable_button.click()
sleep(3)

# find the Remove button
remove_button = driver.find_element(
  By.XPATH, (
    (
        '/html/body/div[2]/div/div[1]/form[1]/button'
        # Example: "//button[text()='Remove']"
    )
  )
)
remove_button.click()
sleep(3)

# find the Add button
# uncomment and replace XPATH
add_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div/div[1]/form[1]/button')
    )
)
add_button.click()
sleep(3)

# find the checkbox
# uncomment and replace XPATH
checkbox = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="checkbox"]')
    )
)
checkbox.click()
sleep(3)

# close the browser and quit the webdriver
driver.quit()

# End-of-file (EOF)
