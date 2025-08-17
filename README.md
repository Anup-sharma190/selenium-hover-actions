# selenium-hover-actions
# Hover Actions Automation Demo

## Project Overview
This project demonstrates **mouse-hover, right-click (context-click), and submenu clicks using Selenium WebDriver**.  
It automates interactions on the **AutomationPractice demo site** and is designed to showcase practical Selenium skills, clean coding, and recruiter-friendly automation projects.

---

## Skills Demonstrated
- Selenium WebDriver setup and configuration
- Implicit waits for stable automation
- Browser window maximization for consistent element visibility
- Complex mouse interactions using **ActionChains**:
  - Mouse hover
  - Right-click (context-click)
  - Move and click submenu items
- Locating elements using different strategies (`ID`, `LINK_TEXT`)
- Writing clean, modular, and readable automation code

---

## Tools Used
- Python 3.x
- Selenium WebDriver
- ChromeDriver
- AutomationPractice demo website: [https://rahulshettyacademy.com/AutomationPractice/](https://rahulshettyacademy.com/AutomationPractice/)

---

## Workflow
1. Initialize Chrome WebDriver and configure implicit waits.
2. Maximize the browser window for stability.
3. Navigate to the AutomationPractice demo page.
4. Prepare **ActionChains** for advanced mouse interactions.
5. Perform the following actions:
   - Hover over the "Mouse Hover" element to reveal submenu.
   - Right-click on the "Top" link.
   - Move to and click the "Reload" link.
6. Wait for visual confirmation of actions.
7. Optionally, close the browser after testing.

---

## How to Use

1. **Clone the repository**:
```bash
git clone <repository_url>
