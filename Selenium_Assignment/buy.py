from selenium import webdriver
driver = webdriver.Chrome(executable_path='/home/shubhama/PycharmProjects/SeleniumBasic/chromedriver')
driver.get("https://www.zillow.com")
assert "Zillow" in driver.title, "Invalid URL"
elem = driver.find_element_by_xpath("//*[@id='page-header-container']/header/nav/div[2]/ul[1]/li[1]")
elem.click()
assert "https://www.zillow.com/homes/" in driver.current_url, "Please Navigate to proper URL"
driver.close()
