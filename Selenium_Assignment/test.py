from selenium import webdriver
driver = webdriver.Chrome(executable_path='/home/shubhama/PycharmProjects/SeleniumBasic/chromedriver')
driver.get("http://www.python.org")
assert "Python" in driver.title, "Invalid URL"
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("__init__")
ele = driver.find_element_by_name("submit")
ele.click()
driver.close()
