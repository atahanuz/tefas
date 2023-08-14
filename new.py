from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

# Setup Chrome options
options = Options()


path="/opt/homebrew/Caskroom/chromedriver/115.0.5790.102/chromedriver-mac-arm64"
# Replace 'path_to_chromedriver' with the actual path where your ChromeDriver is located
driver = webdriver.Firefox()

# The URL you want to navigate to
url = "https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod=AFT"

# Tell the browser to navigate to the URL
driver.get(url)
WebDriverWait(driver, 3)

# Find all the buttons
element = driver.find_element(By.CSS_SELECTOR, 'label[for="MainContent_RadioButtonListFundComparison_0"]')
element.click()

pass



