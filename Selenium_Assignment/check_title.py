from selenium import webdriver
driver = webdriver.Chrome(executable_path='/home/shubhama/PycharmProjects/SeleniumBasic/chromedriver')
driver.get("https://www.zillow.com")
assert "Zillow" in driver.title, "Invalid URL"
driver.close()
