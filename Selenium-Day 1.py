from selenium import webdriver
#Chrome
driver=webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(30)
print(driver.title)

#Firefox
driver1 = webdriver.Firefox()
driver1.get("https://www.facebook.com/")
driver1.maximize_window()
print(driver1.title)

#Edge
driver2 = webdriver.Edge()
driver2.get("https://www.hackerrank.com/")
driver2.maximize_window()
print(driver2.title)






