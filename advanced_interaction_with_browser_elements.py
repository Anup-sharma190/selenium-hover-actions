"""
Hover Actions Automation Demo
-----------------------------
Project: Selenium Mouse Hover & Context Click Demo
File: hover_actions_automation_demo.py

Purpose:
This script demonstrates mouse-hover, right-click (context-click),
and clicking submenu items on a demo web page using Selenium WebDriver
and ActionChains.

Skills Demonstrated:
- Selenium WebDriver setup and configuration
- Implicit waits and browser window management
- Using ActionChains for complex mouse interactions
- Locating elements using ID, LINK_TEXT, and other locators
- Automation of hover menus, context-clicks, and chained actions
- Writing clean, modular, and recruiter-friendly automation code

Tools Used:
- Python 3.x
- Selenium WebDriver
- ChromeDriver
- AutomationPractice demo site (https://rahulshettyacademy.com/AutomationPractice/)

Instructions:
1. Ensure ChromeDriver is installed and added to PATH.
2. Install Selenium library: pip install selenium
3. Run this script to see hover and context-click actions in Chrome.

"""

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# -------------------- Step 1: Initialize WebDriver --------------------
driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
driver.implicitly_wait(5)    # Wait up to 5 seconds for elements to appear
driver.maximize_window()      # Maximize window for stable interactions

# -------------------- Step 2: Navigate to demo page --------------------
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# -------------------- Step 3: Prepare ActionChains --------------------
action = ActionChains(driver)

# -------------------- Step 4: Perform hover, right-click, and submenu click --------------------
# Hover over the element with ID 'mousehover' to reveal submenu
hover_element = driver.find_element(By.ID, "mousehover")
action.move_to_element(hover_element).perform()

# Right-click (context click) on the 'Top' link that appears under the hover menu
top_link = driver.find_element(By.LINK_TEXT, "Top")
action.context_click(top_link).perform()

# Move to the 'Reload' link and click it
reload_link = driver.find_element(By.LINK_TEXT, "Reload")
action.move_to_element(reload_link).click().perform()

# -------------------- Step 5: Wait to visually confirm actions --------------------
time.sleep(10)

# -------------------- Step 6: End of script --------------------
# Uncomment the next line to close the browser automatically after demo
# driver.quit()
