"""
This module demonstrates how to: Drag and drop elements on a webpage
using Selenium.
This example automates the process of dragging an element (Rome)
and dropping it onto another element (Italy).


Author: Arnold Murphy
Date: 2025-04-29
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the demo page
driver.get(
  "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
)

# Wait until the draggable and droppable elements are present
wait = WebDriverWait(driver, 10)
source = wait.until(EC.presence_of_element_located((By.ID, "box6")))  # Rome
target = wait.until(EC.presence_of_element_located((By.ID, "box106")))  # Italy

# Perform drag and drop
actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()
# Optional: Wait to observe the result
time.sleep(3)
time.sleep(3)

# Close the browser
driver.quit()

# End-of-file (EOF)
