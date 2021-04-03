from selenium import webdriver


url = "https://orteil.dashnet.org/cookieclicker/"
chrome_driver_path = r"C:\Users\godle\Documents\chrome_driver_development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=url)
CLICKS1 = 100
CLICKS2 = 2 * CLICKS1
CLICKS3 = 3 * CLICKS1
BUYS = 10
ROUNDS = 30
round_counter = 0


def click_cookie():
    driver.find_element_by_xpath('//*[@id="bigCookie"]').click()


while round_counter <= ROUNDS:
    print(round_counter)
    clicks_per_round = CLICKS1
    print(clicks_per_round)
    print(round_counter)
    if round_counter > 0 and round_counter % 5 == 0:
        CLICKS1 += 100
    # NO UPGRADES USED With the above counter on and ROUNDS set to 30 all time high 'per second' is 74,2 though I've only played it once

    # NO UPGRADES USED With the below counter on and ROUNDS set to 15 all time high 'per second' is 21,4
    # if round_counter >= 10:
    #     clicks_per_round = CLICKS3
    # elif round_counter >= 5:
    #     clicks_per_round = CLICKS2
    # else:
    #     clicks_per_round = CLICKS1
    buy_cooldown = BUYS
    while clicks_per_round >= 0:
        click_cookie()
        clicks_per_round -= 1
    while buy_cooldown >= 0:
        store_items = driver.find_elements_by_class_name("enabled")
        if len(store_items) == 0:
            break
        # Restricting the number of items to save money for more expensive items, only once though just for a kickstart
        try:
            int(driver.find_element_by_id("productOwned2").text)
        except:
            try:
                if int(driver.find_element_by_id("productOwned1").text) >= 8:
                    if len(store_items) < 8:
                        break
            except ValueError:
                click_cookie()
        # I had to include the try-except because I'm not checking anything about the store_items list
        # in this particular project it's much easier to surround 1 line with a simple try-except.
        try:
            store_items[-1].click()
        except:
            click_cookie()
        buy_cooldown -= 1

        # OBSOLETE - a bit messy and unnecessarily complicated
        # num_cookies = driver.find_element_by_xpath('//*[@id="cookies"]').text.split()[0]
        # if float(num_cookies) >= float(store_items[-1].find_element_by_class_name("price").text.replace(",", "")):
        #     store_items[-1].click()
        #     buy_cooldown -= 1
        # elif float(num_cookies) >= float(store_items[-2].find_element_by_class_name("price").text.replace(",", "")):
        #     store_items[-2].click()
        #     buy_cooldown -= 1
        # else:
        #     try:
        #         store_items[-3].click()
        #     except IndexError:
        #         pass
        #     buy_cooldown -= 1
    round_counter += 1