from selenium import webdriver
import time

my_url = "https://www.python.org/"
chrome_driver_filepath = r"C:\Users\godle\Documents\chrome_driver_development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_filepath)
driver.get(url=my_url)
driver.fullscreen_window()
ul_xpath = '/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul'
# Creating the dictionary in a sort of a "java" way
dict_of_events = {}
count = 0
for item in driver.find_element_by_xpath(ul_xpath).find_elements_by_tag_name("li"):
    dict_of_events[count] = {}
    dict_of_events[count]["date"] = item.find_element_by_tag_name("time").text
    dict_of_events[count]["event"] = item.find_element_by_tag_name("a").text
    count += 1
driver.quit()
print(dict_of_events)