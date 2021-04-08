from selenium import webdriver
driver = webdriver.Chrome(executable_path='/home/shubhama/PycharmProjects/SeleniumBasic/chromedriver')
driver.get("https://www.zillow.com")
assert "Zillow" in driver.title, "Invalid URL"
elem = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/header/nav/div[2]/ul")
for i in elem:
    print(i.text)
driver.close()
