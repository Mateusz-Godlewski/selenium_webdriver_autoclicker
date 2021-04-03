from selenium import webdriver


chrome_driver_path = r"C:\Users\godle\Documents\chrome_driver_development\chromedriver.exe"
url = "http://secure-retreat-92358.herokuapp.com/"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=url)
driver.find_element_by_name("fName").send_keys("Twoja")
driver.find_element_by_name("lName").send_keys("Stara")
driver.find_element_by_name("email").send_keys("TwojaStara@Stara.com")
driver.find_element_by_class_name("btn").click()