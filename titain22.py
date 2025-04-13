from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_argument("disable-blink-features=AutomationControlled")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])

  driver = webdriver.Chrome(options=options)
  driver.get("https://titan22.com/account/login?return_url=%2Faccount")
  return driver

def clean_text(text):
  output = float(text.split(": ")[1])
  return output

def main():
  driver = get_driver()
  
  time.sleep(2)
  
  element = driver.find_element(by="id", value="CustomerEmail").send_keys("a@a.com")
  time.sleep(10)
  
  element = driver.find_element(by="id", value="CustomerPassword").send_keys("password" + Keys.RETURN)
  time.sleep(20)
  
  driver.find_element(by="xpath", value='//*[@id="shopify-section-footer"]/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a').click()
  time.sleep(2)
  print(driver.current_url)

  


print(main())
