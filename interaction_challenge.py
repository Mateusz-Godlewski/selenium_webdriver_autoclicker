from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_path = r"C:\Users\godle\Documents\chrome_driver_development\chromedriver.exe"
url = "https://en.wikipedia.org/wiki/Main_Page"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=url)
article_count = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]')
print(article_count.text)
search = driver.find_element_by_name("search")
search.send_keys("python")
search_button = driver.find_element_by_name("go")
search_button.click()