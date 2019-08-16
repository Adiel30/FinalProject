from selenium import webdriver


driver = webdriver.Firefox()

url = "http://localhost:5000/"
driver.get(url)
# Opent the Url and print the body text
siteText = driver.find_element_by_xpath("/html//body")
print ("#" * 60)
print(str(siteText.text))
print ("#" * 60)
driver.close()
