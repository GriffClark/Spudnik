import selenium
import random
from selenium import webdriver
import time
from datetime import datetime

from selenium.webdriver.common.keys import Keys

# driver downloaded from https://sites.google.com/a/chromium.org/chromedriver/downloads

startTime = datetime.now()
print(str(startTime))

"""
TODO
Have bot be able to click links on eCommerce sites
Have bot be able to screenshot all ads it sees
"""
# # INTERNET EXPLORER
# PATH = "C:\Program Files (x86)\IEDriverServer.exe"
# driver = webdriver.Ie(PATH) #hoping that using IE will evade bot detection because... you know... its IE

# # CHROME
# PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)

#Microsoft Edge
PATH = "C:\Program Files (x86)\msedgedriver.exe"
driver = webdriver.Edge(PATH)

def smooth_scroll(target_location):
    scroll_breakup_value = random.randint(10, 50)
    scroll_distance = (target_location - get_current_location()) / scroll_breakup_value
    i = 0
    while i < scroll_breakup_value:
        print(f"\naction " + str(i) + "/" + str(scroll_breakup_value) + " (max)")
        time_sleep_now = random.randint(time_sleep_max/2, time_sleep_max)
        time.sleep(time_sleep_now / 1000)
        if target_location <= get_current_location():
            break
        else:
            location_history.append(get_current_location())
            driver.execute_script("window.scrollBy(" + str(get_current_location()) + "," + str(
                get_current_location() + scroll_distance) + ")", "")
            print(str(int((get_current_location() / get_document_height()) * 100)) + "% done")
            if check_if_stuck():
                # if we're stuck, break out of the loop and restart
                print("smooth scroll claims to be stuck, but it's notorious for lying")
                break
            else:
                print(f"DEBUG: location history: \n" + str(location_history))
        i += 1


def get_current_location():
    return driver.execute_script("return window.pageYOffset;");


def check_if_stuck():
    if len(location_history) > 3 and location_history[-1] == location_history[
        -2]:  # first part is there because first few values will often be 0 as the webpage loads
        print("we're stuck :/ This probably means we reached the end of the page")
        return True
    else:
        return False


def get_location_history():
    return location_history


def open_new_window():
    print("DEBUG: dumping old location history...")
    print(get_location_history())
    print("loading in a new page...")
    website_selection = random.choice(website_list)
    driver.get(website_selection)
    print("clearing location history...")
    global location_history
    location_history = []


def get_document_height():
    return driver.execute_script(
        "return document.body.scrollHeight")  # this has to be recalculated as the webpage loads

# INIT

time_sleep_max = 3500  # in ms
website_list = [
    "https://www.bestbuy.com/site/laptop-computers/all-laptops/pcmcat138500050001.c?id=pcmcat138500050001&qp=parent_operatingsystem_facet%3DOperating%20System~Windows",
    "https://www.bestbuy.com/site/searchpage.jsp?st=macbook&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys",
    "https://www.bestbuy.com/site/searchpage.jsp?st=chromebook&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys",
    "https://www.apple.com/mac/?afid=p238%7CstIisv5mW-dc_mtid_1870765e38482_pcrid_434052220943_pgrid_19485452527_&cid=aos-us-kwgo-mac--slid---product-",
    "https://www.theverge.com/21250695/best-laptops", "https://www.laptopmag.com/reviews/best-laptops-1",
    "https://www.cnet.com/news/best-laptops-of-2020/",
    "https://www.pcmag.com/picks/the-best-laptops",
    "https://www.tomsguide.com/best-picks/best-laptops"]

location_history = []

# sign in to Google so we can make sure we're being tracked
driver.get("https://www.google.com/")
driver.find_element_by_xpath("//*[@id=\"gb_70\"]").click()
driver.find_element_by_xpath("//*[@id=\"identifierId\"]").send_keys("isaacMcCafferty081081@gmail.com")
time.sleep(2)
driver.find_element_by_xpath("//*[@id=\"identifierNext\"]/div/button/div[2]").click()
time.sleep(7)

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys("ea;oiu*&0293%")
driver.get("https://www.google.com/")
time.sleep(5)

while True:
    open_new_window()
    num_scrolls = 0  # resets how many scrolls have been taken on this page
    num_scrolls_to_complete = random.randint(50,
                                             500)  # maximum number of scrolls until we get bored and leave the page, regardless of where we are
    scroll_range_max = get_document_height() / 8  # whats the furthest you can move in one scroll
    default_scroll_value = 800

    while num_scrolls < num_scrolls_to_complete:  # while loop ensures a maximum number of scrolls. If we get to the bottom before then, that's okay too
        # checking to see if we're stuck on a page due to a pop-up

        if get_current_location() >= get_document_height():
            # if you're most of the way through a document that can be far enough
            print("hit the bottom. Restarting this whole kerfluffle over again...")
            break
        else:
            smooth_scroll(random.randint(get_current_location() + default_scroll_value - 100, get_current_location() + default_scroll_value + 100))
            print("default: scrolled down a bit")
            if check_if_stuck():
                # if we're stuck, break out of the loop and restart
                break
        num_scrolls += 1

"""
techradar, laptopmage - moat-skin-tracking
theVerge, - adSize 
pcmag - no class but alt=Advertisement
"""
