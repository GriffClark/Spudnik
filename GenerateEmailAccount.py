from selenium import webdriver
import random
import time

#INTERNET EXPLORER
# PATH = "C:\Program Files (x86)\IEDriverServer.exe"
# driver = webdriver.Ie(PATH) #hoping that using IE will evade bot detection because... you know... its IE

#CHROME
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()

first_name_array = ["Lenny", "Isaac", "Griffin", "Erika", "Hagar", "Lex", "Omar", "Emily", "David", "Michael"]
last_name_array = ["McCline", "McClurn", "Clark", "Bocanegra", "Kousba", "McCafferty", "Shalabi", "Hery", "Detwiller"]

first_name = random.choice(first_name_array)
last_name = random.choice(last_name_array)
identifier = str((random.randint(100000,10000000)))
default_password = first_name + "!" + last_name + "2020" + identifier + first_name

driver.get("https://discover.aol.com/products-and-services/aol-mail")
time.sleep(1)
driver.find_element_by_xpath("//*[@id=\"bbiClose\"]")

